#make sure you install the jotform-api-python from github not just with pip vanilla
#the vanilla pip install doesnt support python3
#pip install git+git://github.com/jotform/jotform-api-python.git


from jotform import *
import pprint
import sys
import yaml
from slugify import slugify  #pip install python-slugify for python3
import unicodedata
import os
import os.path
import urllib
from urllib import request
from urllib import parse
from urllib.parse import urlparse
import time
import getopt

#from urlparse import urlparse    python2

#import requests
from PIL import Image, ExifTags, ImageOps       #pip install pillow (not pil)
import datetime

import os.path
from os import path

eventYear = 2021
outputAll = False

#todo: add command line param to force write all exhibits
#todo: write the exhibit URL back to jotform for easy linking :)
#todo: create a sanitize function that deals with double quotes, etc.
#todo: remove withdrawn / cancelled exhibits...


#image resizing: https://stackoverflow.com/questions/8631076/what-is-the-fastest-way-to-generate-image-thumbnails-in-python

#NOTE: Image pulls will fail unless you go to jotform settings for the account and
#       remove the requirement to be logged in to see uploaded items

# get item from jotform answers list

def getAnswer (sub, id):
  #idStr = str(id).encode("utf-8").decode("utf-8")
  answer = sub["answers"].get(str(id)).get('answer')
  #sanitize any quotes in the answer
  #but don't do it if variable is List or None
  if isinstance(answer, str):
    answer = answer.replace('"', '\\"')

  return answer

# save image locally if not exists
# return local url
def processImage(eid, eslug, type, url):

  a = parse.urlparse(url)
  aFn, aFnExt = os.path.splitext(url)
  #print aFnExt
  last = slugify(aFn.rsplit('/', 1)[-1])
  #print(last)

  base = "../assets/images/exhibit-images/" + eid + "-" + type + "-" + eslug + "-" + last
  fullFn      = base + "-full"    + aFnExt
  smallFn     = base + "-small"   + aFnExt
  mediumFn    = base + "-medium"  + aFnExt
  largeFn     = base + "-large"   + aFnExt

  filenames = (smallFn, mediumFn, largeFn, fullFn)

  if not path.exists(fullFn):
    url = url.replace(" ", "%20")
    print ("Downloading: " + url)
    resource = urllib.request.urlopen(url)
    output = open(fullFn,"wb")
    output.write(resource.read())
    output.close()

  if not path.exists(smallFn):
    # creating a object
    image = Image.open(fullFn)
    image = ImageOps.exif_transpose(image)
    image.thumbnail((150,150))
    image.save(smallFn)

  if not path.exists(mediumFn):
    # creating a object
    image = Image.open(fullFn)
    image = ImageOps.exif_transpose(image)
    image.thumbnail((300,300))
    image.save(mediumFn)

  if not path.exists(largeFn):
    # creating a object
    image = Image.open(fullFn)
    image = ImageOps.exif_transpose(image)
    image.thumbnail((1024,1024))
    image.save(largeFn)

  return filenames

def socialURLClean(url,name):
  social = urlparse(url)
  social = social._replace(scheme = "https")
  social = social._replace(netloc = "www." + name + ".com")
  socialpath = social.path.lower()
  socialpath = socialpath.replace("www." + name + ".com","")
  socialpath = socialpath.replace(name + ".com","")
  #socialpath = socialpath.replace("/","")
  socialpath = socialpath.replace("www.","")
  socialapath = socialpath.replace("www","")
  social = social._replace(path = socialpath)
  return social.geturl()

def urlClean(url):
  site = urlparse(url)
  if site.scheme == "":
    site = site._replace(scheme = "http")
  sitepath = site.path.lower()
  site = site._replace(path = sitepath)
  return site.geturl().replace("///", "//")

def export(outputAll):

    countSubmissions = 0
    countVisible = 0
    countExhibitsRemoved = 0
    countExport = 0

    if path.exists('private.yaml'):
      yamlFile = 'private.yaml'
    else:
      print("Error: Cannot locate settings file")
      sys.exit()

    with open(yamlFile) as settingsFile:
      settings = yaml.load(settingsFile, Loader = yaml.FullLoader)
      #print (settings)

      token = settings['jotform-api-key']
      print ('API Key:  ', token)

    jotformAPIClient = JotformAPIClient(token)

    forms = jotformAPIClient.get_forms()

    for form in forms:
      #print form["title"]
      if form["title"] == "Call For Makers MFO2021":

        #print form
        print(form["id"] + " " + form["title"])
        submissions = jotformAPIClient.get_form_submissions(form["id"], limit = 1000)
        for sub in submissions:
          #print sub
          #sys.exit()

          countSubmissions = countSubmissions+1

          exhibitName = getAnswer(sub,39)
          mfoID = getAnswer(sub,98)

          if exhibitName is None:
            continue

          exhibitName = exhibitName.strip()
          mfoID = mfoID.strip()

          #slugify and remove apostrophes so they don't turn into dashes
          #slug = slugify(exhibitName, replacements = [["'", ""]])  python2
          slug=slugify(exhibitName.replace("'", "")) #python3

          # fName is the full name of the exhibit markdown file
          # Variable established this early so that if exhibit is no longer
          #     visible we can confirm the exhibit file is removed
          fName = "../_exhibits/" + str(eventYear) + "-" +slug + ".md"

          viz = False
          if getAnswer(sub,114) is not None:
            viz = True
            countVisible = countVisible+1

          else:
            if path.exists(fName):
                print("***" + mfoID + " " + exhibitName + " is no longer visible")
                os.remove(fName)
                # print("ALERT: need to remove exhibit file ", fName)
                countExhibitsRemoved = countExhibitsRemoved+1
            continue

          print(mfoID + " " + exhibitName + ": " + str(viz))

          descShort       = getAnswer(sub,40)
          #descShort = descShort.replace('"', '\\"')

          descLong        = getAnswer(sub,41)
          #descLong = descLong.replace('"', '\\"')

          categories      = getAnswer(sub,64)

          exhibitImage    = processImage(mfoID,slug,"exhibit",getAnswer(sub,43)[0])

          exhibitAddlImages = getAnswer(sub,44)

          exhibitVideo    = getAnswer(sub,45)
          exhibitWebsite  = getAnswer(sub,46)
          makerName       = getAnswer(sub,15)
          makerDesc       = getAnswer(sub,16)


          #makerDesc = makerDesc.replace('"', '\\"')

          makerImage      = processImage(mfoID,slug,"maker",getAnswer(sub,18)[0])
          makerEmail      = getAnswer(sub,19)
          makerWebsite    = getAnswer(sub,20)
          makerTwitter    = getAnswer(sub,21)
          makerInstagram  = getAnswer(sub,22)
          makerFacebook   = getAnswer(sub,23)
          makerYouTube    = getAnswer(sub,24)

          # create Exhibit markdown file

          #check to see if last export date > last change date, and then we can skip
          #this will reduce the number of github updates
          export = True

          if path.exists(fName):
            with open(fName) as yFile:
              yData = yaml.load_all(yFile, Loader = yaml.FullLoader)
              #print (yData)
              #parse(yData)
              for data in yData:
                lastExport = data.get('last-exported')
                lastMod = sub["updated_at"]
                #print ('last-exported: ', lastExport)
                #print ('last-modified: ', lastMod)

                dtExport = time.strptime(lastExport, '%Y-%m-%d %H:%M:%S')
                dtMod    = time.strptime(lastMod, '%Y-%m-%d %H:%M:%S')

                export = dtMod > dtExport

                #print ('last-exported: ', dtExport)
                #print ('last-modified: ', dtMod)

                #print (export)

                break
                #only read from the first document

          if export or outputAll:

            countExport = countExport+1
            print("Exporting: " + fName)

            outfile = open(fName, "w")
            outfile.write("---\n")
            outfile.write("# note: title, description, image are used for SEO\n")
            outfile.write("\n")

            #p2 outfile.write("title: " + '"' + exhibitName + '"' + "\n")
            outfile.write("title: " + '"' + exhibitName + '"' + "\n")
            outfile.write("slug: " + slug + "\n")
            outfile.write("permalink: /exhibits/" + slug + "/\n")
            outfile.write("exhibit-id: " + mfoID + "\n")
            outfile.write("description: " + '"' + descShort + '"' + "\n")
            outfile.write("description-long: " + '"' + descLong + '"' + "\n")

            outfile.write("image: "   + exhibitImage[2][2:] + "\n")


            outfile.write("image-primary: \n")
            outfile.write("  small: "   + exhibitImage[0][2:] + "\n")
            outfile.write("  medium: "  + exhibitImage[1][2:] + "\n")
            outfile.write("  large: "   + exhibitImage[2][2:] + "\n")
            outfile.write("  full: "    + exhibitImage[3][2:] + "\n")

            outfile.write("additional-images: \n")

            i=1
            for addlImage in exhibitAddlImages:

              image = processImage(mfoID,slug,"exhibit-addl" + str(i),addlImage)

              outfile.write("  - " + str(i) + ":\n")
              outfile.write("    small: "   + image[0][2:] + "\n")
              outfile.write("    medium: "  + image[1][2:] + "\n")
              outfile.write("    large: "   + image[2][2:] + "\n")
              outfile.write("    full: "    + image[3][2:] + "\n")
              i = i+1


            #Let's stop listing email on the site, too easy to scrape...
            #if makerEmail is not None: outfile.write("email: " + makerEmail + "\n")
            if makerWebsite is not None:
              outfile.write("website: " + urlClean(makerWebsite) + "\n")
            if makerTwitter is not None:
              outfile.write("twitter: " + socialURLClean(makerTwitter, "twitter") + "\n")
            if makerInstagram is not None:
              #insta = urlparse(makerInstagram)
              #insta = insta._replace(scheme = "https")
              #insta = insta._replace(netloc = "www.instagram.com")
              #instapath = insta.path.lower()
              #instapath = instapath.replace("www.instagram.com","")
              #instapath = instapath.replace("instagram.com","")
              #instapath = instapath.replace("/","")
              #instapath = instapath.replace("www.","")
              #instapath = instapath.replace("www","")
              #insta = insta._replace(path = instapath)
              #outfile.write("instagram: " + insta.geturl() + "\n")
              outfile.write("instagram: " + socialURLClean(makerInstagram, "instagram") + "\n")

            if makerFacebook is not None:
              outfile.write("facebook: " + socialURLClean(makerFacebook, "facebook") + "\n")

            if makerYouTube is not None:
              outfile.write("youtube: " + socialURLClean(makerYouTube, "youtube") + "\n")


            #maker info
            outfile.write("maker: \n")
            outfile.write ("  name: " + '"' + makerName + '"' + "\n")
            outfile.write ("  description: " + '"' + makerDesc + '"' + "\n")
            outfile.write ("  image-primary: " + makerImage[1][2:] + "\n")

            #categories
            outfile.write("categories: \n")

            for category in categories:
              outfile.write ("  - slug: " + slugify(category) + "\n")
              outfile.write ("    name: " + category + "\n")

            #metadata
            outfile.write ("created-jotform: " + '"' + sub["created_at"] + '"' + "\n")
            outfile.write ("last-modified-jotform: " + '"' + sub["updated_at"] + '"' + "\n")

            now = datetime.datetime.now()
            outfile.write ("last-exported: " + '"' + now.strftime("%Y-%m-%d %H:%M:%S") + '"' + "\n")

            #don't include in sitemap
            outfile.write ("sitemap: false\n")

            outfile.write("\n---\n")
            outfile.close()

    print("Submissions Found: " + str(countSubmissions))
    print("Submissions Visible: " + str(countVisible))
    print("Exhibits Removed: " + str(countExhibitsRemoved))
    print("Exported: " + str(countExport))

def main():

    outputAll = False

    # Remove 1st argument from the list of command line arguments
    argumentList = sys.argv[1:]

    # Options
    options = "ho:"

    # Long options
    long_options = ["help", "option"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print ("usage: python3 update_exhibits.py [-o option]")
                print ("Options and arguments:")
                print ("-o rebuild :    Rebuild all exhibits")
                sys.exit()

            elif currentArgument in ("-o", "--option"):
                if currentValue == "rebuild":
                    outputAll = True
                    print("opttion: outputAll = ", outputAll)

        export(outputAll)

    except getopt.error as err:
    	# output error, and return with an error code
    	print (str(err))


if __name__ == "__main__":
    main()

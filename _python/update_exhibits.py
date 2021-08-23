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

#from urlparse import urlparse    python2

#import requests
from PIL import Image, ExifTags, ImageOps       #pip install pillow (not pil)
import datetime

import os.path
from os import path

eventYear = 2021



#todo: if instagram, twitter, youtube dont have properly formed URLs, fix them...
#todo: create a sanitize function that deals with double quotes, etc.


#image resizing: https://stackoverflow.com/questions/8631076/what-is-the-fastest-way-to-generate-image-thumbnails-in-python

#NOTE: Image pulls will fail unless you go to jotform settings for the account and
#       remove the requirement to be logged in to see uploaded items


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

def main():

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

          exhibitName = sub["answers"].get(u'39').get('answer')
          mfoID = sub["answers"].get(u'98').get('answer')

          if exhibitName is None:
            continue

          exhibitName = exhibitName.strip()
          mfoID = mfoID.strip()

          viz = False
          if sub["answers"].get(u'114').get('answer') is not None:
            viz = True

          else:
            continue

          #slugify and remove apostrophes so they don't turn into dashes

          #slug = slugify(exhibitName, replacements = [["'", ""]])  python2
          slug=slugify(exhibitName.replace("'", "")) #python3

          print(mfoID + " " + exhibitName + ": " + str(viz))

          descShort       = sub["answers"].get(u'40').get('answer')
          descShort.replace('"', '\\"')

          descLong        = sub["answers"].get(u'41').get('answer')
          descLong = descLong.replace('"', '\\"')

          categories      = sub["answers"].get(u'64').get('answer')

          exhibitImage    = processImage(mfoID,slug,"exhibit",sub["answers"].get(u'43').get('answer')[0])

          exhibitAddlImages = sub["answers"].get(u'44').get('answer')

          exhibitVideo    = sub["answers"].get(u'45').get('answer')
          exhibitWebsite  = sub["answers"].get(u'46').get('answer')
          makerName       = sub["answers"].get(u'15').get('answer')
          makerDesc       = sub["answers"].get(u'16').get('answer')
          makerImage      = processImage(mfoID,slug,"maker",sub["answers"].get(u'18').get('answer')[0])
          makerEmail      = sub["answers"].get(u'19').get('answer')
          makerWebsite    = sub["answers"].get(u'20').get('answer')
          makerTwitter    = sub["answers"].get(u'21').get('answer')
          makerInstagram  = sub["answers"].get(u'22').get('answer')
          makerFacebook   = sub["answers"].get(u'23').get('answer')
          makerYouTube    = sub["answers"].get(u'24').get('answer')

          #create yaml file

          fName = "../_exhibits/" + str(eventYear) + "-" +slug + ".md"


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

          if export:

            countExport = countExport+1
            print("Exporting: " + fName)

            outfile = open(fName, "w")
            outfile.write("---\n")

            #p2 outfile.write("title: " + '"' + exhibitName + '"' + "\n")
            outfile.write("title: " + '"' + exhibitName + '"' + "\n")
            outfile.write("slug: " + slug + "\n")
            outfile.write("permalink: /exhibits/" + slug + "/\n")
            outfile.write("exhibit-id: " + mfoID + "\n")
            outfile.write("description: " + '"' + descShort + '"' + "\n")
            outfile.write("description-long: " + '"' + descLong + '"' + "\n")

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



            #sys.exit()
    print("Exported: " + str(countExport))


if __name__ == "__main__":
    main()

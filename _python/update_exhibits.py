from jotform import *
import pprint
import sys
import yaml
from slugify import slugify
import unicodedata
import os
import os.path
import urllib
from urlparse import urlparse
import requests

import os.path
from os import path

pp = pprint.PrettyPrinter(indent=4, depth=6)

# get api key from yaml
# get folder location from yaml
# get submissions from API
  # if submission is web-visible, then output file

#image resizing: https://stackoverflow.com/questions/8631076/what-is-the-fastest-way-to-generate-image-thumbnails-in-python

#NOTE: Image pulls will fail unless you go to jotform settings for the account and
#       remove the requirement to be logged in to see uploaded items


# save image locally if not exists
# return local url
def processPhoto(eid, eslug, type, url):

  a = urlparse(url)
  aFn, aFnExt = os.path.splitext(url)
  #print aFnExt
  eFn = "../assets/images/exhibit-images/" + eid + "-" + type + "-" + eslug + aFnExt

  if path.exists(eFn):
    print ("Skipping: " + url)
  else:
    print "Downloading: " + url
    resource = urllib.urlopen(url)
    output = open(eFn,"wb")
    output.write(resource.read())
    output.close()

  return eFn


def main():

    countExport = 0

    if path.exists('private.yaml'):
      yamlFile = 'private.yaml'
    else:
      print "Error: Cannot locate settings file"
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
        print form["id"] + " " + form["title"]
        submissions = jotformAPIClient.get_form_submissions(form["id"], limit = 1000)
        for sub in submissions:
          #print sub

          exhibitName = sub["answers"].get(u'39').get('answer')
          mfoID = sub["answers"].get(u'98').get('answer')

          if exhibitName is None:
            continue

          exhibitName = exhibitName.strip()
          mfoID = mfoID.strip()

          viz = False
          if sub["answers"].get(u'114').get('answer') is not None:
            viz = True
            countExport = countExport+1
          else:
            continue

          #slugify and remove apostrophes so they don't turn into dashes
          slug = slugify(exhibitName, replacements = [["'", ""]])

          print mfoID + " " + exhibitName + ": " + str(viz)

          descShort       = sub["answers"].get(u'40').get('answer')
          descLong        = sub["answers"].get(u'41').get('answer')

          categories      = sub["answers"].get(u'64').get('answer')

          exhibitPhoto    = processPhoto(mfoID,slug,"exhibit",sub["answers"].get(u'43').get('answer')[0])


          exhibitAddlPhotos = sub["answers"].get(u'44').get('answer')
          for exhibitAddlPhoto in exhibitAddlPhotos:
            #print exhibitAddlPhoto
            i=1


          exhibitVideo    = sub["answers"].get(u'45').get('answer')
          exhibitWebsite  = sub["answers"].get(u'46').get('answer')
          makerName       = sub["answers"].get(u'15').get('answer')
          makerDesc       = sub["answers"].get(u'16').get('answer')
          makerPhoto      = sub["answers"].get(u'18').get('answer')[0]
          makerEmail      = sub["answers"].get(u'19').get('answer')
          makerWebsite    = sub["answers"].get(u'20').get('answer')
          makerTwitter    = sub["answers"].get(u'21').get('answer')
          makerInstagram  = sub["answers"].get(u'22').get('answer')
          makerFacebook   = sub["answers"].get(u'23').get('answer')
          makerYouTube    = sub["answers"].get(u'24').get('answer')

          #print descShort
          #print descLong
          #print exhibitPhoto
          #print exhibitVideo
          #print exhibitWebsite
          #print makerName
          #print makerDesc
          #print makerPhoto
          #print makerEmail
          #print makerWebsite
          #print makerTwitter
          #print makerInstagram
          #print makerFacebook
          #print makerYouTube

          #create yaml file


          fName = "../_exhibits/" + slug + ".md"
          print "Exporting: " + fName
          outfile = open(fName, "w")
          outfile.write("---\n")
          outfile.write("title: " + '"' + exhibitName.encode("utf8") + '"' + "\n")
          outfile.write("slug: " + slug + "\n")
          outfile.write("permalink: /exhibits/" + slug + "/\n")
          outfile.write("exhibit-id: " + mfoID + "\n")
          outfile.write("description: " + '"' + descShort.encode("utf8") + '"' + "\n")
          outfile.write("description-long: " + '"' + descLong.encode("utf8") + '"' + "\n")
          outfile.write("image: " + exhibitPhoto + "\n")

          outfile.write("categories: \n")

          for category in categories:
            outfile.write ("  - slug: " + slugify(category) + "\n")
            outfile.write ("    name: " + category + "\n")


          outfile.write("\n---\n")
          outfile.close()



          #sys.exit()
    print "Exported: " + str(countExport)


if __name__ == "__main__":
    main()

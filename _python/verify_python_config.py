# Verify you have the required libraries installed
# Execute this python script and confirm no errors are reported

# macos configuration / notes
# Python version is 3.9.6 when this script was developed
#
# Using zsh with the following aliases in ~/.zshrc
#    alias python='python3'
#    alias pip='pip3'

# macos install: these libraries come standard with Python3 on macos 11+
import time
import datetime
import pprint
import sys

import unicodedata

import os
import os.path
from os import path

import urllib
from urllib import request
from urllib import parse
from urllib.parse import urlparse

# macos install: pip install pyyaml
import yaml

# macos install: pip install python-slugify
from slugify import slugify

# macos install: pip install pillow
from PIL import Image, ExifTags, ImageOps

# macos install: pip install git+git://github.com/jotform/jotform-api-python.git
from jotform import *

# See if we can connect to JotForm api and get some submissions
if path.exists('private.yaml'):
  yamlFile = 'private.yaml'
else:
  print("Error: Cannot locate settings file private.yaml located in this directory")
  sys.exit()

with open(yamlFile) as settingsFile:
  settings = yaml.load(settingsFile, Loader = yaml.FullLoader)
  token = settings['jotform-api-key']
  print ('API Key: ', token)

jotformAPIClient = JotformAPIClient(token)
print("Successfully able to establish API connection with JotForm")

forms = jotformAPIClient.get_forms()

countSubmissions = 0

for form in forms:
  if form["title"] == "Call For Makers MFO2021":
    print(form["title"])
    submissions = jotformAPIClient.get_form_submissions(form["id"], limit = 1000)
    for sub in submissions:
      countSubmissions = countSubmissions + 1

print("Submissions Found: " + str(countSubmissions))

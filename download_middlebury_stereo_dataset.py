#!/usr/bin/env python3

import os
import urllib
from bs4 import BeautifulSoup

home = os.path.expanduser("~")
dataset_folder = home + '/Downloads/stereo_dataset'

if not os.path.exists(dataset_folder):
     os.makedirs(dataset_folder)
     os.chdir(dataset_folder)

print(os.getcwd())

source = urllib.request.urlopen('http://vision.middlebury.edu/stereo/data/scenes2014/zip/')
# testfile.retrieve("http://vision.middlebury.edu/stereo/data/scenes2014/zip/Adirondack-imperfect.zip", "Adirondack-imperfect.zip")
soup = BeautifulSoup(source, "lxml")

# for i in soup.findAll('.zip', attrs={'src': re.compile('(?i)(jpg|png)$')}):
#     full_url = urlparse.urljoin(url, i['src'])
#     print "image URL: ", full_url

# print(soup.prettify())
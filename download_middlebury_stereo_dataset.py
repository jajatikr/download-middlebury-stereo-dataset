#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jajati Keshari Routray
# Date Created: Mar 7 2017
# Usage: Download Middlebury stereo dataset
# Requirements: BeautifulSoup, lxml library
# License: MIT
# <https://github.com/jajatikr/download-middlebury-stereo-dataset/blob/master/LICENSE>

# TODO:
# 1. File handling in Windows system, Passing filenames as arguments
# 2. PEP8 formatting
# 3. File download error handling, File already present handling
# 4. File download progressbar
# 5. Use regex in bs4 findAll instead of for loop to remove non-zip elements

import os
import sys
import urllib
from bs4 import BeautifulSoup

# Initialize Dataset directory path
home = os.path.expanduser("~")
dataset_folder = home + '/Downloads/stereo_dataset'

# Check and create Dataset directory
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# Change current working directory to Dataset directory
os.chdir(dataset_folder)

# Read and parse website html
url = 'http://vision.middlebury.edu/stereo/data/scenes2014/zip/'
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source, "lxml")

# [<a href="xyz.zip">xyz.zip</a>, ...] anchor elements
anchor_list = soup.findAll('a')
zip_anchor_list = []

# Remove non-zip anchor elements
for link in anchor_list[:]:
    link_ext = link.get('href')
    if link_ext.endswith('.zip'):
        zip_anchor_list.append(link_ext)

count = 0
print('Downloading...')

for link_ext in zip_anchor_list:
        count += 1
        print('{}/{} : {}'.format(count, len(zip_anchor_list), link_ext))
        urllib.request.urlretrieve(url + link_ext, link_ext)  # retrieve(url, filename)

print('Download complete')

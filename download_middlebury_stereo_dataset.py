#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jajati Keshari Routray
# Date Created: Mar 7 2017
# Usage: Download Middlebury stereo dataset
# Requirements: Python >= 3.4.1, BeautifulSoup, lxml library
# License: MIT

# TODO:
# 1. File download error handling, File already present handling
# 2. File download progressbar
# 3. Use regex in bs4 findAll instead of for loop to remove non-zip elements

import os
import urllib
from bs4 import BeautifulSoup

dataset_folder = input('\nPlease provide dataset directory path to download:\n')

# Check and create Dataset directory
if not os.path.exists(dataset_folder):
    try:
        # Creates folder. Raises error if folder exists or other errors
        os.makedirs(dataset_folder, exist_ok=False)
        print("Created dataset directory : {}".format(dataset_folder))
    except OSError as e:
        # Error printing:
        print('Unable to locate or create provided directory:')
        print('Error No.         : {}'.format(e.errno))
        print('Location          : {}'.format(e.filename))
        print('Error description : {}'.format(e.strerror))
        # Exception handling
        home = os.path.expanduser("~")
        dataset_folder = home + '/stereo_dataset'
        os.makedirs(dataset_folder, exist_ok=True)
        print('\nCreating dataset directory : {}\n'.format(dataset_folder))

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

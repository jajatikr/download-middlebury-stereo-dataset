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

import os
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
for link in soup.findAll('a'):
    link_ext = link.get('href')  # xyz.zip
    if link_ext.endswith('.zip'):
        print('Downloading: ' + link_ext)
        urllib.request.urlretrieve(url + link_ext, link_ext) # retrieve(url, filename)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jajati Keshari Routray
# Date Created: Mar 7 2017
# Usage: Download Middlebury stereo dataset
# Requirements: Python >= 3.4.1
# License: MIT

# TODO:
# 1. File download error handling, File already present handling
# 2. File download progressbar
# 3. Handle URL errors

import os
import re
import urllib.request as url_req
from urllib.error import URLError, HTTPError


def url_response(website):
    try:
        response = url_req.urlopen(website)
        return response
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('Unable to reach the server.')
        print('Reason: ', e.reason)


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
        print('\nCreating default dataset directory : {}\n'.format(dataset_folder))

# Change current working directory to Dataset directory
os.chdir(dataset_folder)

# Read and parse website html
url = 'http://vision.middlebury.edu/stereo/data/scenes2014/zip/'
response = url_response(url)
if response is None:
    quit()
else:
    html = response.read().decode('utf-8')

# [<a href="xyz.zip">xyz.zip</a>, ...] anchor elements
anchor_list = re.findall(r"\"(\w+-\w+\.zip)\"", html)

count = 0
print('Downloading...\n')

for link_ext in anchor_list:
        count += 1
        download_link = url + link_ext
        response = url_response(download_link)
        file_size = float(response.info()['Content-Length']) / 1000000
        print('{:>2}/{} : {:>5} MB | {} '.format(count, len(anchor_list), round(file_size, 1), link_ext))
        url_req.urlretrieve(url + link_ext, link_ext)  # download : retrieve(url, filename)
#       file1_size = os.path.getsize(link_ext)
#       print(file1_size)

print('\nDownload complete\n')

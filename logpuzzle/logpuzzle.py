#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sec(x):
  t = x.split('-')
  t = t[-1].split('.')[0]
  return t

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  website = re.findall(r'_(\S*)',filename)
  f = open(filename,'r')
  text = f.read()
  urls = re.findall(r'GET (\S*puzzle\S*) HTTP',text)
  urls = list(dict.fromkeys(urls))        #removing duplicates
  urls = sorted(urls, key = sec)
  for i in range(len(urls)):
    urls[i] = 'http://'+website[0]+urls[i]
    
  # print(urls[:20])
    
  return urls

def myfn(x):
  return int(x[3:])

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    print("Making directory")
    os.makedirs(dest_dir)
  
  print("Retrieving images...")
  for count,url in enumerate(img_urls):
    urllib.request.urlretrieve(url, os.path.join(dest_dir,'img'+str(count)))
  
  imgs = os.listdir(dest_dir)
  if 'index.html' in imgs:
    imgs.remove('index.html')
  imgs = sorted(imgs, key = myfn)
  
  # Build index.html
  f = open(os.path.join(dest_dir,'index.html'),'w+')
  f.write("<verbatim>\n<html>\n<body>")
  for img in imgs:
    f.write("<img src=\""+os.path.abspath(os.path.join(dest_dir,img))+"\">")
  f.write("</body>\n</html>")


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()

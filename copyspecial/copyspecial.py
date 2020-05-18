#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_path(dir):
  """
  returns a list of the absolute paths of the special files in the given directory
  """
  filenames=os.listdir(dir)
  specials=[]
  for file in filenames:
    if re.findall(r'.*__\w+__.*',file):
      absp = os.path.abspath(os.path.join(dir,file))
      specials.append(absp)
      
  return specials
  
def copy_to(paths,dir):
  """
  given a list of paths, copies those files into the given directory
  """
  abs_to = os.path.abspath(dir)
  # print(abs_to)
  for path in paths:
    shutil.copy(path, abs_to)
  return
  
def zip_to(paths, zippaths):
  """
  given a list of paths, zip those files up into the given zipfile
  """
  # abs_zip = os.path.abspath(zippaths)
  cmd = 'zip -j '+zippaths+' '+' '.join(paths)
  print(cmd)
  subprocess.run(cmd)
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  todir = ''
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  elif args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]


  # +++your code here+++
  # Call your functions
  paths = get_special_path(os.getcwd())
  if todir:
    copy_to(paths, todir)
    
  if tozip:
    zip_to(paths, tozip)
  
if __name__ == "__main__":
  main()

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it                           <h3 align="center">Popularity in 1990</h3>                    Done
 -Extract the names and rank numbers and just print them  <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>  Done
 -Get the names data into a dict and print it                                                                           Done
 -Build the [year, 'name rank', ... ] list and print it                                                                 Done
 -Fix main() to use the extract_names list                                                                              Done
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'r')
  text = f.read()
  f.close()

  year_pat = re.findall(r'(<.+?>Popularity in )(\d+)(<.+?>)',text)
  # print(year_pat[0][1])
  namerank_pat = re.findall(r'(<.+?><.+?>)(\d+)(<.+?><.+?>)(\w+)(<.+?><.+?>)(\w+)(<.+?>)',text)
  nr_dict={}
  for nr in namerank_pat:
    nr_dict[nr[3]]=nr[1]
    nr_dict[nr[5]]=nr[1]
    
  nr_list = [str(year_pat[0][1])]
    
  for k in sorted(nr_dict.keys()):
    nr_list.append(str(k)+" "+str(nr_dict[k]))
    
  # print(nr_list[:20])
  # nr_dict = sorted(nr_dict.keys())
  # print(nr_dict)
  # nr_list = [str(year_pat[0][1])]
  return nr_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  dir = os.getcwd()
  for arg in args:
    fpath = os.path.join(dir,arg)
    try:
      f = open(fpath, 'r')
      f.close()
      nr_list = extract_names(fpath)
    except IOError:
      sys.stderr.write('Problem reading file '+arg)
      
    if summary:
      f = open("summary"+nr_list[0]+".txt","w+")
      for nr in nr_list[1:]:
        f.write(nr+'\n')
      f.close()
      
    else:
      print(nr_list)
  
if __name__ == '__main__':
  main()

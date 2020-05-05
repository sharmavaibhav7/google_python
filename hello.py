#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import re

def repeat(s, exclaim):
  """
  Returns the string 's' repeated 3 times.
  If exclaim is true, add exclamation marks.
  """	
  result=s+s+s
  if exclaim:
    result=result+'!!!'
  return result
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  print('Hello there', sys.argv[1])
  print(repeat('Yay',False))
  print(repeat('Woo Hoo', True))
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  match = re.findall(r'([\w.-]+)@([\w.-]+)',str)

  for mail in match:
    print(mail[0])
    print(mail[1])
  
  # Command line args are in sys.argv[1], sys.argv[2] ...
  # sys.argv[0] is the script name itself and can be ignored
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

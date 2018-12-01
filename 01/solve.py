#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import re

def calc(filename):
  sum = 0
  with open(filename) as file:
    for line in file:
      print line,
      sum += int(line)
    print 'sum:', sum

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

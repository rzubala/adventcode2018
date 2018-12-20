#!/usr/bin/python -tt

import sys
from collections import *

def parse(filename):
  with open(filename) as file:
    for line in file:
      return line.rstrip('\n')

def findPath(res):
  dist = {}
  entry = []
  x = 0  
  y = 0
  px = 0  
  py = 0
  res = res[1:-1]  
  for p in res:
    if p == '(':
      entry.append((x, y))
    elif p == ')':
      x, y = entry.pop()
    elif p == "|":
      x, y = entry[-1]
    else:
      if p == 'W':
        x -= 1
      elif p == 'E':
        x += 1
      elif p == 'N':
        y -= 1
      elif p == 'S':
        y += 1
    
      pd = dist.get((px, py), 0) + 1
      cd = dist.get((x, y), 0)

      if cd:
        dist[(x, y)] = min(cd, pd)
      else:    
        dist[(x,y)] = pd
        
    px = x
    py = y

  print 'number of doors', max(dist.values())
  print 'at least 1000 doors', len([x for x in dist.values() if x >= 1000])

def calc(filename):
  res = parse(filename)
  findPath(res)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

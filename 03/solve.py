#!/usr/bin/python -tt

import sys
import re

def parse(line):
  s = re.search( r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
  id = 0
  x = 0
  y = 0
  w = 0
  h = 0     
  if (s):
    id = int(s.group(1))  
    x = int(s.group(2))  
    y = int(s.group(3))  
    w = int(s.group(4))  
    h = int(s.group(5))
  else:
    print 'Parse error', line  
  return (id, x, y, w, h)

def findMax(parts):
  mX = 0
  mY = 0  
  for p in parts:
    x = p[1] + p[3]
    y = p[2] + p[4]
    if x > mX:
      mX = x
    if y > mY:
      mY = y
  return (mX, mY)

def isOverlap(i, j, parts):
  cnt = 0  
  for p in parts:
    if i >= p[1] and i < p[1] + p[3] and j >= p[2] and j < p[2] + p[4]:
      cnt += 1
    if cnt > 1:
      #print i,j,'->',p,'=',cnt
      return True
  return False  

def findOverlaps(size, parts):
  cnt = 0  
  for i in range(1, size[0]):
    for y in range(1, size[1]):
      if isOverlap(i, y, parts):
        cnt += 1
  return cnt      

def calc(filename):
  parts = []  
  with open(filename) as file:
    for line in file:
      p = parse(line)
      parts.append(p)
  size = findMax(parts)
  print size  
  res = findOverlaps(size, parts)  
  print 'Overlaps:',res  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

#!/usr/bin/python -tt

import sys
import re

def parse(line):
  s = re.search( r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
  if (s):
    id = int(s.group(1))  
    x = int(s.group(2))  
    y = int(s.group(3))  
    w = int(s.group(4))  
    h = int(s.group(5))
    return (id, x, y, w, h)
  else:
    print 'Parse error', line  
    return (0,0,0,0,0)

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
      return True
  return False  

def findOverlaps(size, parts):
  cnt = 0  
  for i in range(1, size[0]):
    for y in range(1, size[1]):
      if isOverlap(i, y, parts):
        cnt += 1
  return cnt      

def isOverlaps(p1, p2):
  l1x = p1[1]
  l1y = p1[2]
  r1x = p1[1] + p1[3] 
  r1y = p1[2] + p1[4]  
  l2x = p2[1]
  l2y = p2[2]
  r2x = p2[1] + p2[3] 
  r2y = p2[2] + p2[4] 
  if l1x<r2x and r1x>l2x and l1y<r2y and r1y>l2y:
    return True
  return False    

def findNotOverlapId(parts):
  l = len(parts)
  overs = []  
  for i in range(0, l):
    p1 = parts[i]
    found = False
    for j in range(i+1, l):
      p2 = parts[j]
      over = isOverlaps(p1, p2)
      found |= over
      if over:
        if p1[0] not in overs:
          overs.append(p1[0])
        if p2[0] not in overs:
          overs.append(p2[0])
    if not found and p1[0] not in overs:
      print 'Found:', p1[0]
      return

def calc(filename):
  parts = []  
  with open(filename) as file:
    for line in file:
      p = parse(line)
      parts.append(p)
  size = findMax(parts)
  #part1
  #res = findOverlaps(size, parts)  
  #print 'Overlaps:',res  
  #part2
  findNotOverlapId(parts)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

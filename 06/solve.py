#!/usr/bin/python -tt

import sys
import re

def dist(f, t):
  return abs(f[0] - t[0]) + abs(f[1] - t[1])

def max(cords):
  x = 0
  y = 0  
  for c in cords:
    if c[0] > x:
      x = c[0]
    if c[1] > y:
      y= c[1]
  return (x+2, y+1)

def readCords(filename):
  cord = []  
  with open(filename) as file:
    for line in file:
        s = re.search( r'(\d+), (\d+)', line)
        if (s):
          x = int(s.group(1))  
          y = int(s.group(2))
          cord.append((x,y))
  return cord    

def findInf(points, size):
  inf = {}  
  for y in range (0, size[1]):
    for x in range (0, size[0]):
      if not (x == 0 or y == 0 or x == size[0]-1 or x == size[1]-1):
        continue
      ind = points.get((x,y))[0]
      if ind > 0:
        inf[ind] = True
  return inf

def findMax(points, size, inf):
    cntInd = {}
    for y in range (0, size[1]):
      for x in range (0, size[0]):
        ind = points.get((x,y))[0]
        if ind in inf or ind == 0:
          continue
        cnt = cntInd.get(ind, 0)
        cntInd[ind] = cnt + 1
    maxInd = sorted(cntInd, key=cntInd.get, reverse=True)[0] 
    print 'max:',maxInd, cntInd[maxInd]    

def calcDist(cords):
  points = {}
  size = max(cords)
  i = 1  
  for c in cords:  
    for y in range (0, size[1]):
      for x in range (0, size[0]):
        p = (x,y)
        d = dist(c,p)
        #print 'cord:',c,'dist:', dist(c, p), p
        cur = points.get(p)
        if cur is None:
          points[p] = (i, d)
        else: 
          oi = cur[0]  
          od = cur[1]
          if od == d:
            oi = 0
          elif d < od:
            oi = i
            od = d
          points[p] = (oi, od)
    i += 1
  inf = findInf(points, size)
  maxCnt = findMax(points, size, inf)  

def calcSumDist(cords):
  points = 0  
  size = max(cords)
  for y in range (0, size[1]):
    for x in range (0, size[0]):
      p = (x,y)
      tot = 0
      for c in cords:
        d = dist(p, c)
        tot += d
        #if tot >= 32:
        if tot >= 10000:
          tot = -1
          break
      if tot > 0:
        points += 1
  print 'Area size', points

def parse(filename):
  cords = readCords(filename)
  #part1
  #dist = calcDist(cords)
  #part2  
  calcSumDist(cords)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  parse(args[0])
  
if __name__ == '__main__':
  main()

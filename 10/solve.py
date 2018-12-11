#!/usr/bin/python -tt

import sys
import re

def parse(line):
  # position=< 3, -2> velocity=<-1,  1>  
  s = re.search( r'position=<([^,]+),([^>]+)> velocity=<([^,]+),([^>]+)>', line)
  if (s):
    x = int(s.group(1))  
    y = int(s.group(2))  
    vx = int(s.group(3))  
    vy = int(s.group(4))
    #print x,y,vx,vy
    return (x, y, vx, vy)
  else:
    print 'Parse error', line,  
    return (0,0,0,0,0)

def getSize(points, t):
  min_x = min(x + t * vx for (x, y, vx, vy) in points)
  max_x = max(x + t * vx for (x, y, vx, vy) in points)
  min_y = min(y + t * vy for (x, y, vx, vy) in points)
  max_y = max(y + t * vy for (x, y, vx, vy) in points)
  return (min_x, max_x, min_y, max_y)

def isPoint(x, y, points, time):
  for p in points:
    if p[0] + time*p[2] == x and p[1] + time*p[3] == y:
      return True 
  return False  

def printPoints(points, time):
  size = getSize(points, time) 
  for y in range(size[2], size[3]+1):
    for x in range(size[0], size[1]+1):
      sys.stdout.write('#') if isPoint(x, y, points, time) else sys.stdout.write('.')
    print    
  print
      
def findMinSize(points):       
  min_time = None
  min_size = None
  for t in range(30000):
    size = getSize(points, t)  
    min_x = size[0]
    max_x = size[1]
    min_y = size[2]
    max_y = size[3]
    size = max_x - min_x + max_y - min_y
    if not min_size or min_size > size:
      min_size = size
      min_time = t
  print 'min time', min_time, min_size  
  return min_time  

def calc(filename):
  points = []  
  with open(filename) as file:
    for line in file:
      p = parse(line)
      points.append(p)
  time = findMinSize(points)  
  printPoints(points, time)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

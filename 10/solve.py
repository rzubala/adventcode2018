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

def getSize(points):
  min_x = min(points)[0]
  max_x = max(points)[0]  
  min_y = min(points, key=lambda item:item[1])[1]
  max_y = max(points, key=lambda item:item[1])[1]  
  return (min_x, max_x, min_y, max_y)

def isPoint(x, y, points, time):
  for p in points:
    if p[0] + time*p[2] == x and p[1] + time*p[3] == y:
      return True 
  return False  

def printPoints(points, time):
  size = getSize(points) 
  for y in range(size[2], size[3]+1):
    for x in range(size[0], size[1]+1):
      sys.stdout.write('#') if isPoint(x, y, points, time) else sys.stdout.write('.')
    print    
  print

def calc(filename):
  points = []  
  with open(filename) as file:
    for line in file:
      p = parse(line)
      points.append(p)
  for t in range (0,5):  
    printPoints(points, t)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

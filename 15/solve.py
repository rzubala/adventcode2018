#!/usr/bin/python -tt

import sys

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      res.append(list(line.rstrip('\n')))
  return res

def findElement(points, elem):
  y = 0 
  res = []  
  for line in points:
    x = 0
    for c in line:
      if c == elem:
        res += [(x, y)]
      x += 1
    y += 1
  return res

def getNextMove(points, p):
  res = []
  x = p[0]
  y = p[1]
  if x > 0:
    xn = x - 1
    res.append((xn,y))
  if x < len(points[y]) - 1:
    xn = x + 1  
    res.append((xn,y))
  if y > 0:
    yn = y - 1
    res.append((x, yn))
  if y < len(points) - 1:
    yn = y + 1  
    res.append((x, yn))
  
  return res  

def fillDistances(points, cnt):
  moves = findElement(points, str(cnt))
  if not moves:
    print 'not found', cnt  
    return
  for m in moves:  
    nextMoves = getNextMove(points, m)
    nextMoves = [p for p in nextMoves if '.' == points[p[1]][p[0]]] 
    for n in nextMoves:
      x = n[0]
      y = n[1]
      points[y][x] = str(cnt+1)
  fillDistances(points, cnt+1)

def getDistances(points, fromP, cnt):
  nextMoves = getNextMove(points, fromP)
  nextMoves = [p for p in nextMoves if '.' == points[p[1]][p[0]]] 

  for n in nextMoves:
    x = n[0]
    y = n[1]
    points[y][x] = str(cnt)

  fillDistances(points, cnt)
  printPoints(points)  

def printPoints(points):    
  for y in points:
    for x in y:
      sys.stdout.write(x)
    print
  print  

def calc(filename):
  points = parse(filename)

  elfs = findElement(points, 'E')
  gobs = findElement(points, 'G')

  getDistances([row[:] for row in points], gobs[0], 1)
    
  printPoints(points)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

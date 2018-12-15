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
    lineStr = ''.join(line)
    res += [(i,y) for i, s in enumerate(lineStr) if s == elem]
    y += 1
  return res

def getNextMoves(points, p, toP):
  res = []
  x = p[0]
  y = p[1]
  dx = toP[0]  
  dy = toP[1]  
  if x > 0:
    xn = x - 1
    if points[y][xn] == '.' or xn == dx and y == dy:
      res.append((xn,y))
  if x < len(points[y]) - 1:
    xn = x + 1  
    if points[y][xn] == '.' or xn == dx and y == dy:
      res.append((xn,y))
  if y > 0:
    yn = y - 1
    if points[yn][x] == '.' or x == dx and yn == dy:
      res.append((x, yn))
  if y < len(points) - 1:
    yn = y + 1  
    if points[yn][x] == '.' or x == dx and yn == dy:
      res.append((x, yn))

  return res  

def findPath(points, fromP, toP, visited, cnt):

  if cnt > 50:
    return None
    
  print fromP, toP, cnt

  visited.append(fromP)  
  nextMoves = getNextMoves(points, fromP, toP) 
  if toP in nextMoves:
    #print 'found', toP
    return cnt
  paths = []  
  for n in nextMoves:
    if n not in visited:
      #print 'goto', n
      path = findPath(points, n, toP, visited[:], cnt+1)
      if path:
        paths.append(path)
  if paths:
    return min(paths)
  return None

def calc(filename):
  points = parse(filename)

  elfs = findElement(points, 'E')
  gobs = findElement(points, 'G')
    
  print findPath(points, elfs[0], gobs[0], [], 0)

  for y in points:
    for x in y:
      sys.stdout.write(x)
    print

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

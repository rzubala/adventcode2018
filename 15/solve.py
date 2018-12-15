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
    return
  for m in moves:  
    nextMoves = getNextMove(points, m)
    nextMoves = [p for p in nextMoves if '.' == points[p[1]][p[0]]] 
    for n in nextMoves:
      x = n[0]
      y = n[1]
      points[y][x] = str(cnt+1)
  fillDistances(points, cnt+1)

def getDistances(points, fromP, toP):
  nextMoves = getNextMove(points, fromP)
  nextMoves = [p for p in nextMoves if '.' == points[p[1]][p[0]]] 
  cnt = 1
  for n in nextMoves:
    x = n[0]
    y = n[1]
    points[y][x] = str(cnt)

  fillDistances(points, cnt)
  #printPoints(points)  
  
  s = points[toP[1]][toP[0]]  
  os = None
  if s == 'E':
    os = 'G'
  else:
    os = 'E'

  nextMoves = getNextMove(points, toP)
  targets = [p for p in nextMoves if points[p[1]][p[0]] == os] 
  if targets:
    return (None, 0)

  nextMoves = [p for p in nextMoves if points[p[1]][p[0]].isdigit()] 
  nextMoves = sorted(nextMoves, key=lambda tup: (tup[1],tup[0]) )
  minmove = None
  result = None
  for n in nextMoves:
    tmp = int(points[n[1]][n[0]])
    if not result or result > tmp:
      result = tmp
      minmove = n
  return (minmove,result)  

def printPoints(points):    
  for y in points:
    for x in y:
      sys.stdout.write(x)
    print
  print  

def calc(filename):
  points = parse(filename)

  printPoints(points) 

  it = 0  
  while True:  
    elfs = findElement(points, 'E')
    gobs = findElement(points, 'G')
    all = sorted(elfs+gobs, key=lambda tup: (tup[1],tup[0]) )
  
    for el in all:
      minmove = None
      minval = None
      os = None
      s = None
      if el in elfs:
        os = gobs
        us = elfs
        s = 'E'
      else:
        os = elfs
        us = gobs
        s = 'G'
      #print 'look',s,el
      #printPoints(points) 
      for o in os:
        pointsd = [row[:] for row in points]
        tomove = getDistances(pointsd, o, el)
        if tomove[1] and (not minval or tomove[1] < minval):
          minmove = tomove[0]
          minval = tomove[1]
      if minmove:    
        #print s,el,'move',minmove, minval
        points[minmove[1]][minmove[0]] = s  
        points[el[1]][el[0]] = '.'

        nus = [x for x in us if x != el]
        nus.append(minmove)
        nus = sorted(nus, key=lambda tup: (tup[1],tup[0]) )

        if el in elfs:
          elfs = nus
        else:
          gobs = nus

    it += 1      
    print it      
    printPoints(points)
    if it > 100:
      break

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

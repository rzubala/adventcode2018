#!/usr/bin/python -tt

import sys

def getPower(x, y, id):
  tmp = ((x+10)*y + id)*(x+10)
  h = int(0 if tmp < 100 else str(tmp)[-3]) - 5
  return h  

def getSquarePower(sx,sy,id,size):
  sum = 0
  for y in range(sy, sy+size):
    for x in range(sx, sx+size):
      tmp = getPower(x,y,id) 
      sum += tmp
  return sum    

def calc(id):
  maxp = 0
  maxx = 0
  maxy = 0  
  for y in range(1, 300-3):
    for x in range(1, 300-3):
      p = getSquarePower(x, y, id,3)
      if p > maxp:
        maxx = x
        maxy = y
        maxp = p
  print 'max',id,'->',maxx, maxy, maxp   

  maxp = 0
  maxx = 0
  maxy = 0  
  maxs = 0  
  for y in range(1, 300+1):
    for x in range(1, 300+1):
      for s in range(1, 300-max(x,y)+2):  
        p = getSquarePower(x, y, id, s)
        if p > maxp:
          maxx = x
          maxy = y
          maxp = p
          maxs = s
  print 'max',id,'->',maxx, maxy, maxs, maxp   

def main():
  calc(7989)
  
if __name__ == '__main__':
  main()

#!/usr/bin/python -tt

import sys

def getPower(x, y, id):
  tmp = ((x+10)*y + id)*(x+10)
  h = int(0 if tmp < 100 else str(tmp)[-3]) - 5
  return h  

def getSquarePower(sx,sy,id):
  sum = 0
  for y in range(sy, sy+3):
    for x in range(sx, sx+3):
      tmp = getPower(x,y,id) 
      sum += tmp
  return sum    

def calc(id):
  maxp = 0
  maxx = 0
  maxy = 0  
  for y in range(1, 300-3):
    for x in range(1, 300-3):
      p = getSquarePower(x, y, id)
      if p > maxp:
        maxx = x
        maxy = y
        maxp = p
  print 'max',id,'->',maxx, maxy, maxp   

def calc1(id):
  print getSquarePower(33,45,18)    
  print getSquarePower(21,61,42)    

def main():
  calc(7989)
  
if __name__ == '__main__':
  main()

#!/usr/bin/python -tt

import sys

def calc(depth, t):
  els = {} 
  rl = 0
  for y in range(0,t[1]+1):
    for x in range(0,t[0]+1):
      if (x,y) == (0,0) or (x,y) == t:  
        gi = 0
      elif y == 0:
        gi = x*16807
      elif x == 0:
        gi = y*48271
      else:
        gi = lastel * els[x]

      el = (gi + depth) % 20183
      lastel = el
      els[x] = el

      if (x,y) == (0,0):
        el = 'M'  
      elif (x,y) == t:
        el = 'T'
      else:  
        if el % 3 == 0:
          el = '.'
          rl += 0
        elif el % 3 == 1:
          el = '='
          rl += 1
        elif el % 3 == 2:
          el = '|'
          rl += 2
  print 'risk level', rl

def main():
  
  #calc(510, (10,10))
  calc(5616, (10, 785))
  
if __name__ == '__main__':
  main()

#!/usr/bin/python -tt

import sys
import networkx

# 0 = nothing, 1 = climbing gear, 2 = torch
def getTools(e):
    if e == 0:        # rocky
      return {1, 2}          # gear, torch
    if e == 1:        # wet
      return {0, 1}       # nothing, gear
    if e == 2:        # narrow
      return {0, 2}       # torch, nothing

def calc(depth, t):
  els = {} 
  cave = {}

  for y in range(0,t[1]+1000):
    for x in range(0,t[0]+1000):
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
      cave[(x,y)] = el % 3
  
  rl = 0
  for y in range(0,t[1]+1):
    for x in range(0,t[0]+1):
      rl += cave[(x,y)]
  print 'risk level', rl

  G = networkx.DiGraph()    #directional graph
  for y in range(0,t[1]+1000):
    for x in range(0,t[0]+1000):
      tools = getTools(cave[(x,y)])
      for tool1 in tools:
        for tool2 in tools:
          if tool1 != tool2:
            G.add_edge((x, y, tool1), (x, y, tool2), weight=7)


def main():
  
  #calc(510, (10,10))
  calc(5616, (10, 785))
  
if __name__ == '__main__':
  main()

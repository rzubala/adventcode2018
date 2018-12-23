#!/usr/bin/python3

import sys
import networkx as nx

# 0 = nothing, 1 = climbing gear, 2 = torch
def getTools(e):
    if e == 0:        # rocky
      return {1, 2}          # gear, torch
    if e == 1:        # wet
      return {0, 1}       # nothing, gear
    if e == 2:        # narrow
      return {0, 2}       # torch, nothing

def findPath(cave, t):
  lx = t[0] + 50
  ly = t[1] + 50
  
  tools = {}
  for y in range(ly):
    for x in range(lx):
      tools[(x, y)] = getTools(cave[(x, y)])

  print('before graph')
  G = nx.DiGraph()    #directional graph

  for y in range(ly):
    for x in range(lx):
      ts = tools[(x, y)]

      for tool1 in ts:
        for tool2 in ts:
          if tool1 != tool2:
            G.add_edge((x, y, tool1), (x, y, tool2), weight=7)

      for (xn, yn) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if (xn,yn) == (x,y) or xn < 0 or yn < 0 or xn >= lx or yn >= ly:
          continue
        tsn = tools[(x,y)]
        tsn = [t for t in tsn if t in ts]
        for tool in tsn:
          G.add_edge((x, y, tool), (xn, yn, tool), weight=1)
    
  print('after graph')
  path = nx.dijkstra_path_length(G, (0, 0, 2), (t[0], t[1], 2))
  print ('path', path)

def calc(depth, t):
  els = {} 
  cave = {}

  lx = t[0] + 50
  ly = t[1] + 50

  for y in range(ly):
    for x in range(lx):
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
  print ('risk level', rl )

  findPath(cave, t)              

def main():
  
  #calc(510, (10,10))
  calc(5616, (10, 785))
  
if __name__ == '__main__':
  main()

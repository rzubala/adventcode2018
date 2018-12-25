#!/usr/bin/python -tt

import sys
import re
import networkx as nx

def distance(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3]- b[3])  

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      s = re.search(r'(.+),(.+),(.+),(.+)', line)
      if s:
        res.append((int(s.group(1)), int(s.group(2)), int(s.group(3)), int(s.group(4))))  
  return res

def calc(filename):
  res = parse(filename)
  g = nx.Graph()
  
  for r in res:
    g.add_node(r)
  
  for a in res:
    for b in res:
      if a == b:
        continue
      if distance(a, b) <= 3:
        g.add_edge(a, b)

  print nx.number_connected_components(g)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

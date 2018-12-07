#!/usr/bin/python -tt

import sys
import re

def getNodes(filename):
  nodes = {}
  with open(filename) as file:
    for line in file:
      s = re.search( r'Step (\w+) must be finished before step (\w+) can begin', line)
      if (s):
        s1 = s.group(1)
        s2 = s.group(2)
        ar = nodes.get(s1, [])
        ar.append(s2)
        ar = sorted(ar)
        nodes[s1] = ar
  return nodes

def getStartNode(nodes):
  tmp = [] 
  first = []  
  for n in nodes:
    for s in nodes[n]: 
      if s not in tmp: tmp.append(s)
  for n in nodes:
    if n not in tmp: 
      first.append(n)
  return sorted(first)

def getLastNode(nodes):
  tmp = []  
  for n in nodes:
    for s in nodes[n]: tmp.append(s)
  for t in tmp:
    if t not in nodes: return t
  return None

def findKeys(nodes, s):
  res = []  
  for n in nodes:
    ar = nodes[n]
    if s in ar:
      res.append(n)
  return res

def findStep(root, nodes, steps):
  if root not in nodes: return []
  st = nodes[root]
  res = []
  for s in st:
    if s not in steps and s in nodes:
      if s not in res: 
        keys = findKeys(nodes, s)
        add = True
        for k in keys:
          if k not in steps:
            add = False
            break
        if add: res.append(s) 
    else:
      tmp = findStep(s, nodes, steps)
      for t in tmp:
        if t not in res: res.append(t)
  return res

def findPath(roots, end, nodes):
  steps = []  
  while True:
    elem = None
    for root in roots:
      if root not in steps:
        res = [root]
      else:
        res = findStep(root, nodes, steps)
      if not res: continue
      res = sorted(res)
      if not elem or res[0] < elem:
        elem = res[0]
    if not elem:
      break
    steps.append(elem)  
  steps.append(end)              
  print 'steps', ''.join(steps)

def parse(filename):
  nodes = getNodes(filename)
  root = getStartNode(nodes)
  last = getLastNode(nodes)
  findPath(root, last, nodes)

  print '***'  
  print root, '->', last  
  for n in nodes:
    print n, ':', ' '.join(nodes[n])    

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  parse(args[0])
  
if __name__ == '__main__':
  main()

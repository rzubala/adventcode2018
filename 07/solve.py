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
  for n in nodes:
    for s in nodes[n]: 
      if s not in tmp: tmp.append(s)
  print ''.join(tmp)  
  for n in nodes:
    if n not in tmp: return n
  return None

def getLastNode(nodes):
  tmp = []  
  for n in nodes:
    for s in nodes[n]: tmp.append(s)
  for t in tmp:
    if t not in nodes: return t
  return None

def findStep(root, nodes, steps):
  if root not in nodes: return []
  print root, '--'  
  st = nodes[root]
  res = []
  for s in st:
    if s not in steps and s in nodes:
      if s not in res: res.append(s)
    else:
      print s, ' <--'  
      tmp = findStep(s, nodes, steps)
      for t in tmp:
        if t not in res: res.append(t)
  return res

def findPath(root, end, nodes):
  steps = [root]  
  while True:
    res = findStep(root, nodes, steps)
    if not res: break
    res = sorted(res)
    steps.append(res[0])  
    print 'found',' '.join(res)
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

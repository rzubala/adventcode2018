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
  return steps                

def isEnd(workers):
  for w in workers:
    if workers[w][1]:
      return False
  return True  

def inprocess(workers):
  result = []  
  for w in workers:
    if workers[w][1]:
      result.append(workers[w][1])
  return result

def getNextTask(roots, last, nodes, done, processing):
  while True:
    elem = None
    for root in roots:
      if root not in done:
        res = [root]
      else:
        res = findStep(root, nodes, done)
      if not res: continue
      filtered = []            
      for r in res:
        if r not in processing:
          filtered.append(r)        
      res = sorted(filtered)
      if not res: continue
      if not elem or res[0] < elem:
        elem = res[0]
    return elem              
    
def countWorkTime(root, last, nodes):
  done = []  
  workers = {}
  for r in range(1,6):
    workers[r] = (0, None) 
  time = 0
  while True:
    for w in workers:
      if not workers[w][1] or workers[w][0] <= time:
        if workers[w][1]:
          done.append(workers[w][1])
        workers[w] = (0, None)
          
        nextTask = getNextTask(root, last, nodes, done, inprocess(workers))

        if nextTask:
          taskTime = time + 60 + ord(nextTask) - ord('A') + 1
          workers[w] = (taskTime, nextTask)
          print time,':', w, nextTask, taskTime  

    if isEnd(workers):     
      print 'Total time:', time + 60 + ord(last) - ord('A')  
      break 
    time += 1

def parse(filename):
  nodes = getNodes(filename)
  root = getStartNode(nodes)
  last = getLastNode(nodes)
  #part1
  steps = findPath(root, last, nodes)
  countWorkTime(root, last, nodes)

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

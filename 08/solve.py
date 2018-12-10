#!/usr/bin/python -tt

import sys

def read(filename):
  with open(filename) as file:
    for line in file:
      return line.split()
      
def calc(data, metadata):
  nodes = int(data[0])
  meta = int(data[1])
  pos = 2   
  nvalue = []   
  if nodes:   
    for n in range(nodes):
      res = calc(data[pos:], metadata)
      pos += res[0]
      nvalue.append(res[1])

  summ = 0
  for m in range(meta):  
    val = int(data[pos])  
    metadata.append(val)
    pos += 1
    if not nodes: 
      summ += val
    else:
      val -= 1
      if val < len(nvalue):
        summ += nvalue[val] 
  return (pos, summ)   

def parse(filename):
  data = read(filename)
  metadata = []  
  res = calc(data, metadata)
  print 'meta', sum(metadata), res[1]  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  parse(args[0])
  
if __name__ == '__main__':
  main()

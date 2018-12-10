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
 if nodes:   
   for n in range(nodes):
     pos += calc(data[pos:], metadata)
 for m in range(meta):   
   metadata.append(int(data[pos]))
   pos += 1
 return pos   

def parse(filename):
  data = read(filename)
  metadata = []  
  calc(data, metadata)
  print 'meta', sum(metadata)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  parse(args[0])
  
if __name__ == '__main__':
  main()

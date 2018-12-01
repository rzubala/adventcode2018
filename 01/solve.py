#!/usr/bin/python -tt

import sys

def calc(filename):
  sum = 0
  intersum = []
  freqs = []  
  rep = False  
  with open(filename) as file:
    for line in file:
      diff = int(line)
      sum += diff
      freqs.append(diff)
      if sum in intersum:
        print 'repetition: ' + str(sum)
        rep = True
      intersum.append(sum)
    print 'sum:', sum
   
  while not rep:
    for f in freqs:
      sum += f
      if sum in intersum:
        print 'repetition: ' + str(sum)
        rep = True
        break

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

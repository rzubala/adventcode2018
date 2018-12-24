#!/usr/bin/python -tt

import sys
import re

def parse(filename):
  res = []
  infection = False
  with open(filename) as file:
    for line in file:
      print line.rstrip('\n')

      s = re.search(r'Infection', line)
      if s:
        infection = True
        continue

      s = re.search(r'(\d+) units .+ with (\d+) hit points (\((.+)\))? ?with an attack that does (\d+) (.+) damage at initiative (\d+)', line)  
      if s:
        units = int(s.group(1))
        hit_points = int(s.group(2))
        weak_immune = s.group(4)
        damage = int(s.group(5))
        damage_type = s.group(6)
        initiative = int(s.group(7))

        weaks = []
        immunes = []

        if weak_immune:
          sw = re.search(r'weak to ([^;]+)', weak_immune)
          if sw:
            weaks = sw.group(1).split(',')

          si = re.search(r'immune to ([^;]+)', weak_immune)
          if si:
            immunes = si.group(1).split(',')

        print infection, units, hit_points, weaks, immunes, damage, damage_type, initiative
        
  return res

def calc(filename):
  res = parse(filename)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()

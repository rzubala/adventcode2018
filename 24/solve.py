#!/usr/bin/python -tt

import sys
import re

def parse(filename):
  res = []
  infection = False
  with open(filename) as file:
    for line in file:
      #print line.rstrip('\n')

      s = re.search(r'Infection', line)
      if s:
        infection = True
        continue

      s = re.search(r'(\d+) units .+ with (\d+) hit points (\((.+)\))? ?with an attack that does (\d+) (.+) damage at initiative (\d+)', line)  
      if s:
        groups = int(s.group(1))
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

        #print infection, groups, hit_points, weaks, immunes, damage, damage_type, initiative
        res.append(Group(infection, groups, hit_points, immunes, weaks, initiative, damage, damage_type))
        
  return res

def calc(filename):
  res = parse(filename)
  fight(res)

def fight(groups_initial):
  #print groups_initial  
  while True:
    groups = sorted(groups_initial, key=lambda g: (g.getEffectivePower(), g.initiative), reverse=True)
    for g in groups:
      print g.getEffectivePower(), g.initiative, g.infection    
    break 

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])

class Group(object):
  def __init__(self, infection, groups, hit_points, immunes, weaks, initiative, damage, damage_type):
    self.infection = infection
    self.groups = groups
    self.hit_points = hit_points
    self.immunes = immunes
    self.weaks = weaks
    self.damage = damage
    self.damage_type = damage_type
    self.target = None
    self.initiative = initiative,

  def getEffectivePower(self):
    return self.groups * self.damage

  def getDamage(self, enemy):
    if self.damage_type in enemy.immunes:
      return 0
    elif self.damage_type in enemy.weaks:
      return self.getEffectivePower() * 2
    else:
      return self.getEffectivePower()
  
if __name__ == '__main__':
  main()

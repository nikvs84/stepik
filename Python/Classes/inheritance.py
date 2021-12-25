# put your python code here

import sys

glob = {}


def parse(line):
    global glob
    arr = line.split(' : ')
    clazz = arr[0]
    if len(arr) > 1:
        parents = arr[1].split(' ')
        if clazz in glob:
            glob[clazz] = glob.get(clazz).append(parents)
        else:
            # parents.append(clazz)
            glob[clazz] = parents
    else:
        glob[clazz] = []


def isParent(parent, clazz):
    parentSet = glob.get(clazz)
    if parentSet is None:
        return False
    
    if parent == clazz:
        return True

    # print('Check is ' + parent + ' in [' + ', '.join(parentSet) + ']')
    if parent in parentSet:
        return True
    else:
        if len(parentSet) > 0:
            for par in parentSet:
                # print('Check is ' + parent + ' parent of ' + par)
                if isParent(parent, par):
                    return True
        else:
            return False


sys.stdin = open('resources/set_3.txt')

n = int(input())
for i in range(n):
    line = input()
    parse(line)

# print(glob)

q = int(input())

for i in range(q):
    line = input()
    arr = line.split(' ')
    parent = arr[0]
    clazz = arr[1]
    print('Yes' if isParent(parent, clazz) else 'No')
    
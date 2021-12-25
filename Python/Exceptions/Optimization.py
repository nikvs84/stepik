# import sys

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


def is_parent(parent, clazz):
    parent_set = glob.get(clazz)
    if parent_set is None:
        return False

    if parent == clazz:
        return True

    # print('Check is ' + parent + ' in [' + ', '.join(parentSet) + ']')
    if parent in parent_set:
        return True
    else:
        if len(parent_set) > 0:
            for par in parent_set:
                # print('Check is ' + parent + ' parent of ' + par)
                if is_parent(parent, par):
                    return True
        else:
            return False


def has_parent(ex_class, candidates):
    for clazz in candidates:
        if is_parent(clazz, ex_class):
            return True
    return False


# sys.stdin = open('resources/test_1.txt')

for i in range(int(input())):
    parse(input())

# print(glob)

already_used = []

for i in range(int(input())):
    ex = input()
    if ex not in already_used and not has_parent(ex, already_used):
        already_used.append(ex)
    else:
        print(ex)


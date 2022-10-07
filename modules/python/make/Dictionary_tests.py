
from Dictionary import *


# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @


# * gen_letters ----------------------------------------------------------
# + ------------------WORKING-------------------- +

d = Dictionary({})

print('\n# Testing "gen_letters":')
print('\nDefault:\n\n', d.gen_letters())
print('\nInput "l":\n\n', d.gen_letters('l'))
print('\nInput "u":\n\n', d.gen_letters('u'))
print('\nInput "a":\n\n', d.gen_letters('a'))

# * group ----------------------------------------------------------
# + ------------------WORKING-------------------- +

seq = Dictionary('pontchartrain')

print('\n# Testing "group":\n')
# print('# Before:\t', seq)
# print('# After:\t', seq.group())
print(seq, '\t->\t', seq.group())

# * ungroup ----------------------------------------------------------
# + ------------------WORKING-------------------- +

d1 = Dictionary({'a': 2, 'b': 1, 'z': 3})

print('\n# Testing "ungroup":\n')
# print(d1.ungroup())  # expected: a a b z z z
print(d1, '\t->\t', d1.ungroup())

# * merge ----------------------------------------------------------
# + ------------------WORKING-------------------- +

d3 = Dictionary({"imagine": 1, "and": 2, "make": 3})
d4 = Dictionary({"one": 4, "from": 5, "two": 6})

print('\n# Testing "merge":\n')
# print(d3.merge(d4))
print(d3, '\t+\t', d4, '\t->\t', d3.merge(d4))

# * substractVals --------------------------------------------------
# + ------------------WORKING-------------------- +

d5 = Dictionary({'h': 1, 'e': 1, 'l': 2, 'o': 1,
                'a': 10, 'b': 9, 'c': 8, 'd': 7})
d6 = Dictionary({'h': 1, 'e': 1, 'l': 1, 'o': 1})

# Concise
print('\n# Testing "subtractVals":\n')
print(d5.subtractVals_v1(d6), '\t# v1')
print(d5.subtractVals(d6), '\t# v2')

# todo: clean up the format of the below test
# Descriptive
# print('# TECHNIQUE—1: for loop\n\t# Updated d1:\n\t', d5.subtractVals_v1(d6))
# print('\n\t# d2 is subset of d1:\n\t', d5.subtractVals_v1(d6))
# print('\n# TECHNIQUE—2: list comprehension\n\t# Updated d1:\n\t',
#       d5.subtractVals(d6))
# print('\n\t# d2 is subset of d1:\n\t', d5.subtractVals(d6))

# * isSupersetOf ---------------------------------------------------
# + ------------------WORKING-------------------- +

print('\n# Testing "isSupersetOf":\n')
print(f"{d5.isSuperSetOf_v1(d6)}\t# Expected:\t\tTrue\t# v1")
print(f"{d5.isSuperSetOf_v2(d6)}\t# Expected:\t\tTrue\t# v2")
print(f"{d5.isSuperSetOf(d6)}\t# Expected:\t\tTrue\t# v3")

# * swap_KeyVal ----------------------------------------------------
# + ------------------WORKING-------------------- +
print('\n# Testing "swap_KeyVal":\n')
print('# Before:\t', d1)
print('# After:\t', d1.swap_KeyVal())
#  ------------------END TEST---------------------

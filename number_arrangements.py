# given two numbers a and b we need to arrange 
# a in all possible ways and print the number which 
# is just greater than b

from itertools import permutations

value, compare = input().split()

compare = int(compare)
b = str(compare)
a = str(value)
a = ''.join(sorted(a))

if len(a) < len(b):
    print(-1)
else:
    result = -1
    permlist = permutations(a)
    for i in permlist:
        str1 = "".join(i)
        n = int(str1)
        if n > compare:
            result=n
            break
    print(result)
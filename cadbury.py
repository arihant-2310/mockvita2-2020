a = int(input())
b = int(input())
c = int(input())
d = int(input())
total =0
def find_total(a, b):
    if a == b:
        return 1
    if b == 1:
        return a
    diff = a - b
    return 1+find_total(max(diff,b),min(diff,b))
for i in range(a, b + 1):
    for j in range(c, d + 1):
        total = total + find_total(max(i, j), min(i, j))
print(total)
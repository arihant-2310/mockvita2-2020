number = int(input())

# initialize the matrix
c = [[0 for x in range(number)] for y in range(number)]

#initialize list to store power points
#power points are the multiples of 11
p = list()
p.append((0, 0))

#initialize the start and end
start = 0
end = number - 1

n = 1

#the total number of spirals will be n(n+1)/2
#repeat the outer loop that number of times
for i in range(int((number+1)/2)):
    for j in range(start,end+1):
        c[start][j] = n
        if (n % 11 == 0):
            p.append((start, j))
        n = n + 1
    for j in range(start + 1, end + 1):
        c[j][end] = n
        if (n % 11 == 0):
            p.append((j, end))
        n = n + 1
    for j in range(end-1,start-1,-1):
        c[end][j] = n
        if (n % 11 == 0):
            p.append((end,j))
        n = n + 1
    for j in range(end-1,start,-1):
        c[j][start] = n
        if (n % 11 == 0):
            p.append((j,start))
        n = n + 1
    
    start = start + 1
    end = end-1


#print the chakravyuha matrix
for i in range(number):
    for j in range(number):
        print(c[i][j], end="\t")
    print()

# print the power points
print("The total power points:", len(p))
print(*p,sep="\n")

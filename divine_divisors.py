# to write a program to print all the divisors of a number
divisors = list()
def divine_divisors(n):
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            print(i,end=" ")
            if n//i != i:
                divisors.append(int(n / i))
    divisors.sort()
    print(*divisors,end=" ")
n= int(input())
divine_divisors(n)

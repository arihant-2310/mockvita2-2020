# the problem is to given the value of n, we need to distribute coins
# of 1 rs, 2 rs, 5 rs in such a way that the number of coins is minimized
# and any value between 1 and n can be formed using those coins

def coins(n):
    five_rs_coins = (n - 4) // 5
    if (n - 5 * five_rs_coins) % 2==0:
        one_rs_coins = 2
    else:
        one_rs_coins = 1
    two_rs_coins = (n - 5 * five_rs_coins - one_rs_coins) // 2
    total_coins = five_rs_coins+two_rs_coins+one_rs_coins
    print(total_coins,five_rs_coins,two_rs_coins,one_rs_coins)

print("Enter the value of the money:")
n = int(input())
coins(n)
    
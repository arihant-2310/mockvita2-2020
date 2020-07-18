t = int(input())
while (t > 0):
    n = int(input())
    monkeys = list(map(int, input().split(' ')))
    initial_list = []
    initial_list2 = []
    previous_list = [0]*n
    cnt = 0
    while True:
        for i, value in enumerate(monkeys):
            if cnt == 0:
                previous_list[value - 1] = i + 1
                initial_list2.append(i+1)
            else:
                previous_list[value - 1] = initial_list[i]
        initial_list = previous_list.copy()
        if previous_list == initial_list2:
            break
        cnt += 1
    t -= 1
    print(cnt+1)

N = int(input())
brides_to_be = input()
grooms_to_be = input()

brides = list(brides_to_be)
grooms = list(grooms_to_be)
end = False

while end==False:
    if brides[0] == grooms[0]:
        brides.pop(0)
        grooms.pop(0)
        N = N - 1
    elif len(grooms) <= 0:
        end = True
    else:
        i = 0
        while(i<len(grooms)-1):
            if grooms[0] not in brides:
                end = True
                break
            groom = grooms.pop(0)
            grooms.append(groom)
            i = i + 1
            if i >= len(grooms):
                end = True
            
print(len(grooms))



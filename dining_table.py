# dining table seating arrangements
tables, peoples = input().split(" ")
tables = int(tables)
peoples = int(peoples)
if tables >= peoples:
    print(1)
else:
    PA = peoples // tables
    PB = PA + 1
    TB = peoples % tables
    TA = tables - TB
    
    factorials = list((1, 1))
    for i in range(2, peoples + 2):
        x = i * factorials[i - 1]
        factorials.append(x)
    
    divide = factorials[peoples] / ((factorials[PA]**TA) * (factorials[PB]**TB) * (factorials[TA]) * (factorials[TB]))
    
    if PB >= 4:
        arrange = int(divide * ((factorials[PA - 1]/2)**TA) * (factorials[PB - 1]/2)**TB)
    else:
        arrange = divide
print(arrange)
    
    

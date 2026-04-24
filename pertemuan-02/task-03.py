def oddDetector(var):
    return var % 2 == 0

def WhileOdd(rng):
    i = 0
    while (i < rng):
        if (oddDetector(i) == False):
            print(i)
        i += 1

def ForEven(rng):
    for i in range(rng):
        if (oddDetector(i) == True):
            print(i)
print("Odd num :")
WhileOdd(10)
print('\nEven num :')
ForEven(10)

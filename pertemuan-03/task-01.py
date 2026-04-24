from array import array as arr

num = arr('Q', [4, 6, 8, 3, 4, 3, 6, 4, 5, 40])

def display():
    print("|", end='')
    for i in num:
        print(i, end='|')
    print('\n')

npm = int(input("Input NPM\n> "))
num.append(npm)
print('\nnormal array:')
display()

find = num.count(4)
print(f"This number ({find}) appears {find} times\n")

num.reverse()
print("reversed array:")
display()

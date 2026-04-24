stack = ['The Ego and Its Own']

def display(data):
    print('Books in shelf:')
    for i in data:
        print(i)

def pushAll(data):
    for i in data:
        stack.append(i)
        print(f'{i} is added')

def isEmpty(data):
    if len(data) == 0:
        print(f"{data} is empty")
    else:
        print("Shelf is not empty")


data = ['Beyond Good and Evil', 'Thus Spoke Zarathustra', 'Politeia']

isEmpty(stack)
print('\n')
pushAll(data)
print('\n')
display(stack)
print('\n')
pop = stack.pop()
print(f"{pop} is deleted")
print('\n')
size = len(stack)
print(f"There's {size} books in the shelf")

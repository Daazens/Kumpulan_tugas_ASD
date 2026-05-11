def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            print(f'check {data[j]} {data[j + 1]}')
            if data[j] > data[j + 1]:
                print(f'swapped - {data[j]} {data[j + 1]}')
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data

inp = str(input('input number\n> '))
data = []
for i in inp.split():
    data.append(int(i))

print('list:')
for i in data:
    print(i, end = ' ')
print()

bubble_sort(data)
for i in data:
    print(i, end = ' ')

data = [67, 89, 23, 10, 56]

def selection_sort(list):
    for i in range(len(list) - 1):
        max_idx = i 
        for j in range(len(list) - 1, i, -1 ):
            print(f'check {list[j]} <> {list[max_idx]}')
            if (list[j] < list[max_idx]):
                max_idx = j
        if (max_idx != i):
            print(f'swapped {list[i]} <> {list[max_idx]}')
            list[i], list[max_idx] = list[max_idx], list[i]
    return list

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            print(f'check id {i + 1} > {list[j]}|{list[j + 1]}')
            if list[j] < list[j + 1]:
                print(f'swapped > {list[j]} {list[j + 1]}')
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list
print('bubble = 1 and selection = 2')
select = str(input("sort?\n>"))
if select == '2':
    bubble_sort(data)
    print(data)
elif select == '1':
    selection_sort(data)
    print(data)
else:
    print('invalid')

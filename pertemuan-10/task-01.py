list = [29, 19, 90, 76, 39, 87, 105, 22, 15, 33, 97, 100, 11, 7, 45]
look = 87
start = 0
end = len(list) -1
found = False

def linear_search(list, look):
    data = -1
    for i in range(len(list)):
        print(f'{list[i]}|{i}')
        if list[i] == look:
            data = i
            break

    if data == -1:
        print('data not found\n')
    else:
        print(f'data found at index {data}\n')

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

def binary_search(list, look, start, end, found):
    while not found and start <= end:
        search = (start + end) // 2
        print(f'{list[search]}|{search}')
        if list[search] == look:
            found = True

        elif list[search] > look:
            end = search - 1 
        else:
            start = search + 1 

    if found:
        print(f'data found at index {search}\n')
    else:
        print('data not found\n')

linear_search(list, look)
bubble_sort(list)
print('list sorted\n')
binary_search(list, look, start, end, found)

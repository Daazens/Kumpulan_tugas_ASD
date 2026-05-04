'''
nama ada Atma[43], Raya[56], Nirmala[70], Erik[29], Lulu[33], Marin[65], Admiral[48]
33 = name?
data != linear
'''

name_data = ["Atma", "Raya", "Nirmala", "Erik", "Lulu", "Marin", "Admiral"]
nim_data = [43, 56, 70, 29, 33, 65, 48]
look = 33
start = 0
end = len(nim_data) - 1 
found = False

def linear_search(nim, name,look):
    step = 0
    for i in range(len(nim)):
        step += 1
        if nim[i] == look:
            print(f'lama > {step}')
            print(f'data > {name[i]}|{nim[i]}')

def bubble_sort(data1, data2):
    for i in range(len(data1)):
        for j in range(len(data1)):
            if data1[i] < data1[j]:
                temp1 = data1[i]
                data1[i] = data1[j]
                data1[j] = temp1
                temp2 = data2[i]
                data2[i] = data2[j]
                data2[j] = temp2

def binary_search(data1, data2, look, start, end, found):
    step = 0
    while not found and start <= end:
        search = (start + end) // 2 
        step += 1
        if data1[search] == look:
            found = True
        elif data1[search] > look:
            end = search - 1 
        else:
            start = search + 1 
    if found:
        print(f'lama > {step}')
        print(f'name > {data2[search]}|{data1[search]}')
    else:
        print('not found')

print('Linear search')
linear_search(nim_data, name_data, look)

print('\nBinary search (sorted by bubble sort)')
bubble_sort(nim_data, name_data)
binary_search(nim_data, name_data, look, start, end, found)

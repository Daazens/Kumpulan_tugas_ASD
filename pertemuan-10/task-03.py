'''
nama ada Atma[43], Raya[56], Nirmala[70], Erik[29], Lulu[33], Marin[65], Admiral[48]
33 = name?
data != linear > linear search
'''
data = [
        ["Atma", 43],
        ["Raya", 56],
        ["Nirmala", 70],
        ["Erik", 29],
        ["Lulu", 33],
        ["Marin", 65],
        ["Admiral", 48]
        ]

look = 33
start = 0
end = len(data) - 1
found = False

def linear_search(data, look):
    step = 0
    find = ''
    for i in range(len(data)):
        step += 1
        if data[i][1] == look:
            find += f'{data[i][0]}|{data[i][1]}\nstep > {step}'
            return find
    return None

def bubble_sort(data):
    step = 0
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            step += 1
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return step

def binary_search(data, look, start, end, found):
    step = 0
    find = ''
    while not found and start <= end:
        step += 1
        search = (start + end) // 2 
        if data[search][1] == look:
            found = True
            find += f'{data[search][0]}|{data[search][1]}\nstep > {step}'
            return find
        elif data[search][1] > look:
            end = start - 1
        else:
            start = end + 1
    return None

linear = linear_search(data, look)
print(f'linear:\n{linear}')


step = bubble_sort(data)
print(f'\nsorted by bubble sort\n')

binary = binary_search(data, look, start, end, found)
print(f'binary:\n{binary} + {step} (sorting)')


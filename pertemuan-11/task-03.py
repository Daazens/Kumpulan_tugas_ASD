data = ['Rimaya', 'Zabrilla', 'Rayhan', 'Fanissa', 'Yulia', 'Rose', 'Arif', 'Esti']
def selection_sort(data):
    for i in range(len(data) - 1):
        max_idx = i 
        for j in range(len(data) -1, i, -1):
            if data[j] < data[max_idx]:
                max_idx = j
        if max_idx != i:
            data[i], data[max_idx] = data[max_idx], data[i]

    return data
alp = 'a'
s = 0
count = chr(ord(alp) + s)
selection_sort(data)
for i in data:
    count = chr(ord(alp) + s)
    print(f'{count}|{i}')
    s += 1
    

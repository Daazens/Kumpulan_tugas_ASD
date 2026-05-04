'''
desa ada Syafi'[28], Zakir[32], Iqbal[45], Rose[48], Gita[52], Hilma[57], Ratih[60]. 
Kannisa[28] > orang baru Q> look = 28+ (lebih tua darinya)
data == linear > binary search? look tidak spesifik > linear search!
'''
data = [
        ["Syafi'", 28],
        ["Zakir", 32],
        ["Iqbal", 45],
        ["Rose", 48],
        ["Gita", 52],
        ["Hilma", 57],
        ["Ratih", 60]
        ]
look = 28

def linear_search(look, data):
    result = ''
    list = []
    for i in range(len(data)):
        if data[i][1] > look:
            result = f'{data[i][0]}|{data[i][1]}'
            list.append(result)
    return list

Quest = linear_search(look, data)
print('List people who are older than Kannisa:')
for i in Quest:
    print(i)        

'''
desa ada Syafi'[28], Zakir[32], Iqbal[45], Rose[48], Gita[52], Hilma[57], Ratih[60]. 
Kannisa[28] > orang baru > look = 28+ (lebih tua darinya)
data = linear
'''
name_data = ["Syafi'", "Zakir", "Iqbal", "Rose", "Gita", "Hilma", "Ratih"]
age_data  = [28, 32, 45, 48, 52, 57, 60]
look = 28

def linear_search(Age, Name, look):
    for i in range(len(Age)):
        if Age[i] > look:
            print(f'{Name[i]}|{Age[i]}')

print('Older than Kannisa:')
linear_search(age_data, name_data, look)

class Model:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def __str__(self):
        return f'{self.name} | {self.file}'

class Printer:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        return self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def get_data(self):
        return self.queue

p = Printer()

lazy_name = ['Dazzen', 'Isaac', 'Joseph']
lazy_file = ['astrologi articles', 'paper', 'alchemy articles', 'thesis']
for i in range(4):
        data = Model(lazy_name[i], lazy_file[i])
        p.enqueue(data)
        print('data added')

while True:
    print('1.add user (enqueue)')
    print('2.file printed (dequeue)')
    print('3.get Q length (size)')
    print('4.is printer empty? (isEmpty)')
    print('5.display (print all user)')
    print('6.exit')
    select = str(input('>'))
    match(select):
        case '1':
            name = str(input("Name? >"))
            file = str(input("File? >"))
            data = Model(name, file)
            p.enqueue(data)
            print(f'{data} is added to Q\n')

        case '2':
            try:
                data = p.dequeue()
                print(f'{data.name} is done\n')
            except IndexError:
                print(f'no one using printer\n')

        case '3':
            print(f'Q length is {p.size()}\n')

        case '4':
            if p.isEmpty() == False:
                print("there's someone using printer\n")
            else:
                print("printer Q is empty\n")
        case '5':
            for data in p.get_data():
                print(data)
            print('')

        case '6':
            break

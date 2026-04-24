class Model:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"-{self.name}"

class Manager:
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

m = Manager()

lazy_data = ['data', 'data', 'data']
for i in lazy_data:
    add = m.enqueue(Model(i))
    print(f'{i} is added to Q')

print('')
while True:
    print("1.add people (enqueue)")
    print('2.serve people (dequeue)')
    print('3.get Q length (size)')
    print('4.check people (isEmpty)')
    print('5.display (print all name)')
    print('6.exit')
    select = str(input('>'))
    match(select):
        case '1':
            name = str(input("Name? >"))
            data = Model(name)
            m.enqueue(data)
            print(f'{name} is added to Q\n')

        case '2':
            try:
                print(f'{m.dequeue()} is served\n')
            except IndexError:
                print('every one is served\n')


        case '3':
            print(f'Q length is {m.size()}\n')

        case '4':
            if (m.isEmpty == True):
                print("Q is empty\n")
            else:
                print("there's someone in Q\n")

        case '5':
            for name in m.get_data():
                print(name)
            print('')

        case '6':
            break


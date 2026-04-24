class Model:
    def __init__(self, url, title, time):
        self.url = url
        self.title = title
        self.time = time

    def __str__(self):
        return f'{self.url}|{self.title}|{self.time}'

class Web:
    def __init__(self):
        self.stack = []

    def push(self, data):
        return self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def get_data(self):
        return self.stack

w = Web()

model1 = Model("google.com", "google tanslate", '20:00')
model2 = Model("wikipedia.org", "geospatial intelligence", '20:20')
model3 = Model('wikipedia.org', 'geospatial', '21:02')
lazy = [model1, model2, model3]
for i in lazy:
    w.push(i)

while True:
    print("1.push")
    print("2.pop")
    print("3.size")
    print("4.peek")
    print("5.isEmpty")
    print("6.displpay")
    print("7.exit")
    select = str(input(">"))
    match(select):
        case '1':
            url = str(input("URL? "))
            title = str(input("Page title? "))
            time = str(input("time? "))
            data = Model(url, title, time)
            w.push(data)
            print(f'{data} added to history')

        case '2':
            data = w.pop()
            print(f'{data} is deleted')

        case '3':
            print(f'page length is {w.size()}')

        case '4':
            if not w.isEmpty():
                print(w.peek())
            else:
                print('page is empty')

        case '5':
            data = w.isEmpty()
            if data == False:
                print("page is not empty")
            else:
                print('page is empty')
        
        case '6':
            for data in w.get_data():
                print(data)

        case '7':
            break


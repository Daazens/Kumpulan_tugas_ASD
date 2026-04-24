class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'{self.name} by {self.author}'

class Shelf:
    def __init__(self):
        self.stack = []

    def push(self, name, auth):
        book = Book(name, auth)
        return self.stack.append(book)

    def pop(self):
        return self.stack.pop()

    def get_data(self):
        return self.stack

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

s = Shelf()
if (s.isEmpty()):
    print("Stack is Empty\n")

s.push("No Longer Human", "Osamu Dazai")
s.push("Notes from Underground", "Fyodor Dostoevsky")
s.push("The Metamorphosis", "Franz Kafka")

for i in s.get_data():
    print(i) 

print(f"\nStack length :{s.size()}\n")

s.pop()

for i in s.get_data():
    print(i)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def insert_before(self, temp_node, new_data):
        if temp_node is None:
            return

        new_node = Node(new_data)

        new_node.prev = temp_node.prev
        temp_node.prev = new_node
        new_node.next = temp_node

        if new_node.prev is not None:
            new_node.prev.next = new_node

        if temp_node == self.head:
            self.head = new_node

    def delete_head(self):
        if self.head is None:
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

        print()

nim = #isi nim#

dll = DoubleLinkedList()

dll.append(nim)
dll.append(nim + 2)

print('NIM ditambahkan:')
dll.display()

x = nim + 21
dll.push(x)

print("\nX ditambahkan:")
dll.display()

y = nim * 2

last = dll.head
while last.next:
    last = last.next

dll.insert_before(last, y)

print("\nY ditambahkan:")
dll.display()

dll.delete_head()
print("\nHasil akhir:")
dll.display()

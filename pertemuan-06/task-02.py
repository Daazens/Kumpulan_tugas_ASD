class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def __str__(self):
        result = ""
        pointer = self.head
        while pointer != None:
            result = result + str(pointer.data) + " "
            pointer = pointer.nextNode
        return result

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def add_first(self):
        node = Node(data, self.head)
        self.head = node

    def add_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def add(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.add_first(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def remove_first(self):
        if (self.get_length() > 0):
            if (self.get_length() == 1):
                value = self.head.data
                self.head = None
                return value
            else:
                pointer = self.head
                value = self.head.data
                self.head = pointer.next
                pointer.next = None
                return value
        return None

    def remove_last(self):
        if (self.get_length() > 0):
            if (self.get_length() == 1):
                value = self.head.data
                self.head = None
                return value
            else:
                pointer = self.head
                while pointer.next.next != None:
                    pointer = pointer.next
                value = pointer.next.data
                pointer.next = None
                return value
            return None

    def add_values(self, data_list):
        self.head = None
        for data in data_list:
            self.add_last(data)


lls = LinkedList()

lazy_data = ['Rimaya', 'Rose', 'Zabrila', 'Yoegi', 'Yulia', 'Fanissa', 'Rosalia', 'Januar', 'Rahayu', 'Daruna']

lls.add_values(lazy_data)
lls.remove_at(9)
lls.remove_at(7)
lls.remove_at(3)
lls.print()
print(f'Mahasiswa aktif yang tersisa ada {lls.get_length()} orang')





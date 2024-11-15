class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        nb = Node(data)         # nb = node at beginning
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)         # ne = node at end
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne


    def display(self):
        if self.head is None:
            print('list is empty')

        else:
            temp = self.head
            while temp:
                print(f'{temp.data} ----->', end=' ')
                temp = temp.next
            print('None')

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

l = SinglyLinkedList()
l.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
l.insert_beginning(100)
l.insert_end(999)

l.display()


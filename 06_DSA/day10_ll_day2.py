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

# day3 starts here
    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

# deletion
    def delete_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_last(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_pos(self, pos):
        prev = self.head
        temp = self.head.next
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next



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
l.insert_position(3, 111)
# l.delete_first()
# l.delete_last()
# l.delete_pos(3)

l.display()



print('=========================== my way ==========================================')
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_last(self, data):
        ne = Node(data)
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
                print(f'{temp.data} ==>', end=" ")
                temp = temp.next
            print('khatam')


sll = SLL()
sll.display()
sll.insert_at_beg(10)
sll.insert_at_beg(5)
sll.insert_at_last(15)
sll.display()
'''
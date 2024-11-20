# circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self, data):
        nb = Node(data)
        # following 4 lines are mandatory for insrt beg/end

        # when CLL is empty
        if self.head is None:
            self.head = nb
            self.tail - nb
            self.tail.next = self.head
        # when CLL is not empty
        else:
            nb.next = self.head
            self.tail.next = nb
            self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        # when CLL is empty
        if self.head is None:
            self.head = ne
            self.tail - ne
            self.tail.next = self.head
        # when CLL is not empty
        temp = self.tail
        ne.next = temp.next
        temp.next = ne



    def display(self):
        if self.head is None:
            print('it is empty')
        else:
            temp = self.head
            print(temp.data, '====>', end=' ')
            while temp.next != self.head:
                temp = temp.next
                print(temp.data, '====>', end=' ')
            # print(temp.next.data)


cll = CLL()

n1 = Node(100)
cll.head = n1
cll.tail = n1
cll.tail.next = cll.head

n2 = Node(200)
cll.tail.next = n2
cll.tail = n2
cll.tail.next = cll.head

cll.insert_beg(0)
cll.insert_end(999)

cll.display()


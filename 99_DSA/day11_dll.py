class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end=' ')
                temp = temp.next
            print('None')

    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    #     below, why?
        nb.prev = self.head
        self.head = nb

    def insert_last(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

    def insert_pos(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        np.prev = temp
        np.next = temp.next
        temp.next = np

    def delete_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

# TODO:    delete last
# TODO:    delete pos

dll = DLL()

n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)

dll.head = n1
n1.next = n2
n1.prev = None
n2.next = n3
n2.prev = n1
n3.next = n4
n3.prev = n2

dll.display()
dll.insert_beg(10)
dll.insert_last(999)
dll.display()
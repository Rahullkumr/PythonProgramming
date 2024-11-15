# Linked List
"""
- It is a collection of group of Nodes
Each node contains data and reference(pointer) which contains the address of next node
here--->Node--->data + reference
it is a linear data structure
elements are stored randomly

why linked list?
ll is having more efficiency for performing the operations as compared to list
elements are stored randomly whereas in list at continuous memory
accessing the elements in linked list will be slower as compared to list
utilization of memory is higher than list

Types of Linked List:
1. Singly ll
- it is traversed in one direction

diagram: head = (data+reference) ---> (data+reference) ---> (data+None)


- operation that can be performed are:
    - insertion:
        - beginning
        - at specified node
        - at end
    - deletion:
        - beginning
        - at specified node
        - at end

Traversal ==> going through each node of the ll

2. Doubly ll
- it is a collection of nodes in which each node contains data field and having two pointers
- one pointer is for previous node and other for next node
- traversal is in forward as well as backward direction

diagram: head= (None+data+reference) <---> (previous+data+reference) <---> (previous+data+None)

- operation that can be performed are:
    - insertion:
        - beginning
        - at specified node
        - at end
    - deletion:
        - beginning
        - at specified node
        - at end
3. Circular ll
- last node contains the address of first node

diagram: head = (address of last node+data+reference) <---> (previous+data+reference) <---> (previous+data+address of first node)


"""
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp

    def insert_middle(self, data, after_value):
        temp = Node(data)
        curr = self.head
        while curr and curr.value != after_value:
            curr = curr.next
        if curr:
            temp.next = curr.next
            curr.next = temp
            if temp.next is None:
                self.tail = temp

    def insert_end(self, data):
        temp = Node(data)
        if not self.tail:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=' -> ')
            curr = curr.next
        print('None')

# Example usage:
ll = LinkedList()
ll.insert_start(10)
ll.insert_start(5)
ll.insert_end(20)
ll.insert_middle(15, 10)
ll.display()

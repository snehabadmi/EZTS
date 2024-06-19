class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None  # Add a prev pointer

# Create the singly linked list
Head = Tail = Node(10)
Tail.next = Node(20)
Tail = Tail.next
Tail.next = Node(30)
Tail = Tail.next
Tail.next = Node(30)
Tail = Tail.next
current = Head
while current.next:
    current.next.prev = current
    current = current.next
current = Head
while current:
    print(f"Node:",current.value)
    print(f"prev:",current.prev.value if current.prev else None)
    current = current.next

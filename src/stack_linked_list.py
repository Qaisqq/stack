class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

class StackLinkedList:
    def __init__(self):
        self.list = LinkedList()

    def is_empty(self):
        return self.list.is_empty()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            return None
        temp = self.list.head.data
        self.list.head = self.list.head.next
        return temp

    def peek(self):
        if self.is_empty():
            return None
        return self.list.head.data

    def __repr__(self):
        current = self.list.head
        stack_str = "Stack:\n"
        while current:
            stack_str += f"| {current.data} |\n"
            current = current.next
        stack_str += "----\n"
        return stack_str 
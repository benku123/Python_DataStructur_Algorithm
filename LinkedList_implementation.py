class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None
        self.index = 0

    def append(self, val):
        new = Node(val)

        if not self.start_node:
            self.start_node = new
            return

        last = self.start_node
        while last.ref:
            last = last.ref
        last.ref = new

        self.index += 1

    def insert(self, index, value):
        start_counting = 0
        start = self.start_node
        NewNode = Node(value)

        if index == 0: # Handling the position 0 case.
            NewNode.ref = start
            self.start_node = NewNode
        else:
            while start_counting < index - 1: # Iterating until the previous node.
                start_counting += 1
                start = start.ref

            tmp = start.ref
            start.ref = NewNode
            NewNode.ref = tmp


    def display(self):
        ls = []
        last = self.start_node
        while last:
            ls.append(last.item)
            last = last.ref
        return ls


s = LinkedList()
s.append(32)
s.append(23)
s.append(3222)
s.append(42)
s.insert(1, 2)
print(s.display())

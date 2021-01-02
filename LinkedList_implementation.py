class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def append(self, val):
        new = Node(val)
        if not self.start_node:
            self.start_node = new
            return

        last = self.start_node
        while last.ref:
            last = last.ref
        last.ref = new

    def display(self):
        last = self.start_node
        while last.ref is not None:
            print(last.item)
            last = last.ref
        print(last.item)


s = LinkedList()
s.append(32)
s.append(23)
s.append(42)
print(s.display())



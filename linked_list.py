class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_item = Node(value)
        new_item.next = self.head
        self.head = new_item

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.value == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.value == item:
                found = True
            elif current.next is None:
                return
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

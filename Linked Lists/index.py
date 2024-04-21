# Constructor
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# Linked List
class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        temp = self.head
        pre = self.head

        if self.length == 0:
            return None

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value


new_linked_list = LinkedList(1)

new_linked_list.append(2)
new_linked_list.append(3)
# new_linked_list.append(4)
# new_linked_list.append(5)
# new_linked_list.append(6)

print(new_linked_list.pop())
print(new_linked_list.pop())
print(new_linked_list.pop())
print(new_linked_list.pop())

# new_linked_list.print_list()

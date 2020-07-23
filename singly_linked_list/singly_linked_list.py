class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            # if self.head is None and self.tail is None
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None
        # lis with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # list with +2 Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # consider same edge cases as remove head
        # 1. empty list
        if self.tail is None:
            return None
        # 2. list with one node
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.tail = None
            self.head = None
            self.length -= 1
        # 3. list with two or more nodes
        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_next()
            self.length -= 1
            return value

    def contains(self, value):
        if self.head is None:
            return None
        visited_node = self.head
        while visited_node is not None:
            if visited_node.get_value() == value:
                return True
            visited_node = visited_node.get_next()
        return False

        # 1. use a loop to iterate through the LL
        # 2. check if the value of the current node is the value we are searching for
        # 3. return True if we find it, False if we reach the end of the LL

    def get_max(self):
        # empty list
        if self.head is None:
            return None
        # non-empty list
        # iterate through all nodes
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max

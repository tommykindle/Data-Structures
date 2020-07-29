"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    """
    Rearranges this ListNode's previous ad next pointers
    accordingly, effectively deleting this ListNode.
    """

    def delete(self):
        if self.prev:
            next_node = self.prev
            next_node.next = self.next
        if self.next:
            next_node = self.next
            next_node.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.length <= 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        removedHead = self.head
        if not self.head:
            return None
        else:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return removedHead.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        newTail = ListNode(value)
        if self.length <= 0:
            self.head = newTail
            self.tail = newTail
            self.length += 1
        else:
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail
            self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        removedTail = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return removedTail.value
    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node == self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node == self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1

        if not self.head and not self.tail:
            return

        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None

        elif self.head == node:
            self.head = self.head.next
            node.delete()

        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()

        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        maxValue = self.head.value
        visited = self.head.next
        while visited:
            if visited.value > maxValue:
                maxValue = visited.value
            visited = visited.next
        return maxValue

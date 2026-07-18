class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        # The value this node holds
        self.data = data
        # Pointer to the next node in the list - starts empty since
        # we don't know what comes after yet
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        # An empty list has no head (no first node) yet
        self.head = None

    def insert_at_front(self, data):
        # Wrap the data in a new Node
        new_node = Node(data)
        # The new node's "next" should point to whatever was
        # previously the first node (could be None if list was empty)
        new_node.next = self.head
        # Now the new node officially becomes the head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty, the new node just becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk from the head until we find the last node
        # (the one whose .next is None)
        current = self.head
        while current.next is not None:
            current = current.next

        # Attach the new node after the last one
        current.next = new_node

    def recursive_sum(self):
        # Kick off the recursion starting from the head
        return self._sum_helper(self.head)

    def _sum_helper(self, node):
        # Base case: an empty node contributes nothing
        if node is None:
            return 0
        # Recursive case: this node's data, plus the sum of everything after it
        return node.data + self._sum_helper(node.next)

    def recursive_reverse(self):
        # Start the helper with prev=None (nothing behind the first node)
        # and current=self.head (start from the front)
        self.head = self._reverse_helper(None, self.head)

    def _reverse_helper(self, prev, current):
        # Base case: we've walked off the end of the list.
        # 'prev' is now the last node we touched, which becomes
        # the new head of the reversed list.
        if current is None:
            return prev

        # Save a reference to the next node BEFORE we overwrite it
        next_node = current.next

        # Flip this node's pointer to point backward instead of forward
        current.next = prev

        # Move one step forward: what was "current" becomes the new "prev",
        # and what was "next_node" becomes the new "current"
        return self._reverse_helper(current, next_node)

    def recursive_search(self, target):
        return self._search_helper(self.head, target)

    def _search_helper(self, node, target):
        # Base case: ran off the end of the list without finding it
        if node is None:
            return False
        # Base case: found it
        if node.data == target:
            return True
        # Recursive case: keep looking in the rest of the list
        return self._search_helper(node.next, target)

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) + " -> None")
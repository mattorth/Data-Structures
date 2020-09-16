class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        # updating head and tail attributes
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        elif self.head == self.tail:
            # update its pointer
            new_node.set_next_node(self.head)
        else:
            # set next_node of my new node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # Create a new node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is not empty
        else:
            # update current tail next node
            # update self.tail
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else return value of old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with 2+ elements
            else:
                self.head = self.head.get_next_node()
            return ret_value


    def remove_tail(self):
        # TODO
        pass

    def contains(self, value):
        # TODO time permitting
        pass
    def get_max(self):
        # TODO time permitting
        pass
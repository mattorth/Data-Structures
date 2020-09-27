from LinkedList import LinkedList, Node
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        ret_value = None
        if self.size > 0:
            ret_value = self.storage[0]
            self.storage.pop(0)
            self.size -= 1
        return ret_value

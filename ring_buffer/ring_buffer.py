from singly_linked_list import LinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = LinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_end(item)
            self.current = self.storage.tail
        else:
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.storage.insert_after(self.current, item)
                self.current = self.current.next_node

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next_node
        return list_buffer_contents

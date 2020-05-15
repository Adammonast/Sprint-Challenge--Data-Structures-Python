# from singly_linked_list import LinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = LinkedList()

#     def append(self, item):
#         if len(self.storage) < self.capacity:
#             self.storage.add_to_end(item)
#             self.current = self.storage.tail
#         else:
#             if self.current == self.storage.tail:
#                 self.storage.remove_from_head()
#                 self.storage.add_to_head(item)
#                 self.current = self.storage.head
#             else:
#                 self.storage.insert_after(self.current, item)
#                 self.current = self.current.next

#     def get(self):
#         list_buffer_contents = []
#         node = self.storage.head
#         while node:
#             list_buffer_contents.append(node.value)
#             node = node.next
#         return list_buffer_contents

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def remove(self):
        if self.next_node:
            self.next_node = None


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.node_removed = None

    def append(self, item):
        # check the capacity to see if full, if not:
        if self.length < self.capacity:
            self.length += 1
            # check if the head already exists, if not create and set its value to itself
            if self.head == None:
                self.head = Node(item)
                self.head.next_node = self.head
            # check for existing nodes, move through looking for the second to last one
            else:
                # add a new node and make it the node_removed
                current = self.head
                while current.next_node is not self.head:
                    current = current.next_node
                current.next_node = Node(item)
                current = current.next_node
                current.next_node = self.head
                self.node_removed = current
        else:
            # set up a new node to be removed
            to_be_removed = self.node_removed.next_node.next_node
            # specific node being removed
            removed = self.node_removed.next_node
            self.node_removed.next_node = Node(item)
            if self.head == removed:
                self.head = self.node_removed.next_node
            removed.remove()
            self.node_removed = self.node_removed.next_node
            # set up another node to be removed
            self.node_removed.next_node = to_be_removed

    def get(self):
        list_buffer_contents = []
        current = self.head
        while current.next_node is not self.head:
            list_buffer_contents.append(current.value)
            current = current.next_node
        list_buffer_contents.append(current.value)
        return list_buffer_contents

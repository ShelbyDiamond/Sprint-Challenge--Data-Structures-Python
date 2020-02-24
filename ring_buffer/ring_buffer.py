from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.__len__(): # if RingBuffer has room, Add newest item to head
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    # pseudocode
    # if the len of the storage is less then the capacity of the linked list
    # then we're going to access storage and add item to tail
    # then we are going to assign the current node to be at the tail of the linked list

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        num = 0
        while num < self.storage.__len__():  #loop through storage
            current_head = self.storage.head  # head
            list_buffer_contents.append(current_head.value)  # append head value to list
            self.storage.move_to_end(current_head)  # move head to tail
            num += 1  # record that iteration and then start over
        return list_buffer_contents
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
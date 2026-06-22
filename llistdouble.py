class Node:
    # 1. Added 'p' for the previous node, defaulting to None
    def __init__ (self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p  # <-- New attribute

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    # 2. Added getter and setter for the previous node
    def get_prev (self):
        return self.prev_node

    def set_prev (self, p):
        self.prev_node = p

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class DoublyLinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        # Create new node pointing forward to the current root
        new_node = Node (d, self.root, None)
        
        # 3. If there is already a root, point its 'prev' back to our new node
        if self.root:
            self.root.set_prev(new_node)
            
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root

        while this_node:
            if this_node.get_data() == d:
                next_node = this_node.get_next()
                prev_node = this_node.get_prev()  # Look backward using the node itself!

                # 4. Handle the forward pointer from the previous node
                if prev_node:
                    prev_node.set_next(next_node)
                else:
                    self.root = next_node  # We are removing the root node

                # 5. Handle the backward pointer from the next node
                if next_node:
                    next_node.set_prev(prev_node)

                self.size -= 1
                return True  # data removed
            else:
                # Move to the next node
                this_node = this_node.get_next()
                
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    
myList = DoublyLinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size=" + str(myList.get_size()))  # size=3
myList.remove(8)
print("size=" + str(myList.get_size()))  # size=2
print(myList.remove(12))                 # True
print("size=" + str(myList.get_size()))  # size=1
print(myList.find(5))                    # 5
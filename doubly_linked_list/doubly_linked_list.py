"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
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
        if self.head:
            new_node = ListNode(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        else:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head
            self.length += 1
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #if there are multiple nodes
        if self.head and self.head.next:
            old_head = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return old_head.value
        elif self.head:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        else:
            return None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail:
            #capture old tail and instantiate new tail
            old_tail = self.tail
            new_tail = ListNode(value, old_tail)

            #update old tail's next value and append the new tail to the list
            old_tail.next = new_tail
            self.tail = new_tail
            self.length += 1
        else:
            new_tail = ListNode(value)
            self.head = new_tail
            self.tail = new_tail
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #if the list contains multiple nodes
        if self.tail and self.tail.prev:
            old_tail = self.tail
            new_tail = self.tail.prev

            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return old_tail.value
        #if the list contains a single node
        elif self.tail:
            tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return tail.value
        else:
            return None

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev
            self.length -= 1

        # if not self.head and not self.tail:
        #     return
        # if self.head is self.tail:
        #     self.head = None
        #     self.tail = None
        # elif self.head is node:
        #     self.head = node.next
        #     node.delete()
        # elif self.tail is node:
        #     self.tail = node.prev
        #     node.delete()
        # else:
        #     node.delete()
        # self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head and self.head.next:
            current = self.head.next
            max_value = self.head.value
            while current:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            return max_value
        elif self.head:
            return self.head.value
        else:
            return None

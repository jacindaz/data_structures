class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def linked_list_values(self):
        current_node = self.head
        linked_list_values = [current_node.val]
        while current_node.next != None:
            current_node = current_node.next
            linked_list_values.append(current_node.val)

        return linked_list_values

    def insert_node(self, prior_node_val, new_node_val):
        new_node = Node(new_node_val)

        current_node = self.head
        while current_node != None:
            if current_node.val == prior_node_val:
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    def insert_at_tail(self, new_node_val):
        new_node = Node(new_node_val)

        if self.head is None:
            self.head = new_node
            tail = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            old_tail = current_node

            old_tail.next = new_node
            tail = new_node

        return tail.val

    def insert_at_head(self, new_node_val):
        new_node = Node(new_node_val)
        new_node.next = self.head
        self.head = new_node

node_12 = Node(12)
node_92 = Node(92)
node_26 = Node(26)
node_1 = Node(1)

node_12.next = node_92
node_92.next = node_26
node_26.next = node_1

ll = LinkedList(node_12)
# print(ll.insert_at_tail(100))
# print(ll.insert_at_head(100))

print(ll.insert_node(92, 100))
print(ll.linked_list_values())


# Traverse a linked list
# Remove duplicates from a linked list
# Get the kth to last element from a linked list
# Delete a node from a linked list
# Add two linked lists from left to right
#  e.g. 1->2->3 + 8->7 => 321+78 = 399
# Add two linked lists from right to left
#  e.g. 1->2->3 + 8->7 => 123+87 = 210

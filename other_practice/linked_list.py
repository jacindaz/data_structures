class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

node_12 = Node(12)
node_92 = Node(92)
node_26 = Node(26)
node_1 = Node(1)

node_12.next = node_92
node_92.next = node_26
node_26.next = node_1


class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert_node(self, prior_node, new_node):
        print('insert node')

    def insert_at_tail(self, new_node):
        print('insert at tail')

    def insert_at_head(self, new_node):
        new_node.next = self.head
        self.head = new_node

ll = LinkedList(node_12)
print(ll.head.val)

new_node = Node(100)
ll.insert_at_head(new_node)


# Traverse a linked list
# Remove duplicates from a linked list
# Get the kth to last element from a linked list
# Delete a node from a linked list
# Add two linked lists from left to right
#  e.g. 1->2->3 + 8->7 => 321+78 = 399
# Add two linked lists from right to left
#  e.g. 1->2->3 + 8->7 => 123+87 = 210

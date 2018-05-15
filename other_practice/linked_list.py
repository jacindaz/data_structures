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
linked_list = [node_12, node_92, node_26, node_1]

def reverse_linked_list(linked_list):

    print('hi!')

# Traverse a linked list
# Remove duplicates from a linked list
# Get the kth to last element from a linked list
# Delete a node from a linked list
# Add two linked lists from left to right
#  e.g. 1->2->3 + 8->7 => 321+78 = 399
# Add two linked lists from right to left
#  e.g. 1->2->3 + 8->7 => 123+87 = 210

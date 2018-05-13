#!/usr/bin/python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(node, mini=float('-inf'),maxi=float('inf')):
  # if node is None, that means reached leaf
  # and didn't find node that was invalid
  # so return True
  if node is None:
    return True

  # if node is less than min or node is greater than max
  # return false
  # because means that node is a left child and is bigger than parent
  # or means that node is right child and is smaller than parent
  # which is invalid for a binary search tree
  if node.data < mini or node.data > maxi:
    return False

  # otherwise, recurse
  # if going down left sub-tree:
  #  => recurse using left child
  #  => change max to be parent, because child cannot be greater than the parent
  #  => leave min as is, because as long as child isn't greater than parent,
  #     child node can be as small as you want
  #
  # if going down right sub-tree:
  #  => recurse using right child
  #  => change min to be parent, because child cannot be less than the parent
  #  => leave max as is, because as long as child is not less than parent,
  #     child node can be as big as you want
  return (is_bst(node.left, mini, node.data)) and (is_bst(node.right, node.data, maxi))

def main():
    # nodes = int(sys.stdin.readline().strip())
    # tree = []
    # for i in range(nodes):
    #     tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # tree: [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
    # tree data = [4,2,1,5]
    # left: [1,2,-1,-1]
    # right: [-1,3,-1,-1]
    # -1 means no child

    # not BST
    # root = Node(4)
    # root.left = Node(2)
    # root.left.left = Node(1)
    # root.left.right = Node(5)

    # yes BST
    # root = Node(2)
    # root.left = Node(1)
    # root.right = Node(3)

    if is_bst(root):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

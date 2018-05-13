# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def __init__(self):
        self.read()
        self.in_order_results = []
        self.pre_order_results = []
        self.post_order_results = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root, root_index=0):
        if root_index == -1:
            return

        if len(self.key) > 0:
            left_child_indices = self.left[root_index]
            left_child = self.key[left_child_indices]

            self.inOrder(left_child, left_child_indices)
            self.in_order_results.append(root)

            right_child_indices = self.right[root_index]
            right_child = self.key[right_child_indices]
            self.inOrder(right_child, right_child_indices)

        return self.in_order_results

    def preOrder(self, root, root_index=0):
        if root_index == -1:
            return

        if len(self.key) > 0:
            self.pre_order_results.append(root)

            left_child_indices = self.left[root_index]
            left_child = self.key[left_child_indices]
            self.preOrder(left_child, left_child_indices)

            right_child_indices = self.right[root_index]
            right_child = self.key[right_child_indices]
            self.preOrder(right_child, right_child_indices)

        return self.pre_order_results

    def postOrder(self, root, root_index=0):
        if root_index == -1:
            return

        if len(self.key) > 0:
            left_child_indices = self.left[root_index]
            left_child = self.key[left_child_indices]
            self.postOrder(left_child, left_child_indices)

            right_child_indices = self.right[root_index]
            right_child = self.key[right_child_indices]
            self.postOrder(right_child, right_child_indices)

            self.post_order_results.append(root)

        return self.post_order_results

def main():
    tree = TreeOrders()

    print(" ".join(str(x) for x in tree.inOrder(tree.key[0])))
    print(" ".join(str(x) for x in tree.preOrder(tree.key[0])))
    print(" ".join(str(x) for x in tree.postOrder(tree.key[0])))

threading.Thread(target=main).start()

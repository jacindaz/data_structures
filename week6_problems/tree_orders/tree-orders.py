# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def __init__(self):
        self.read()
        self.results = []

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
            print(f'\ninside if statement, root: {root}, {self.pre_order_results}')

            left_child_indices = self.left[root_index]
            left_child = self.key[left_child_indices]
            print(f'left_child: {left_child}, root: {root}, {self.pre_order_results}')

            self.preOrder(left_child, left_child_indices)

            right_child_indices = self.right[root_index]
            right_child = self.key[right_child_indices]
            print(f'right_child: {right_child}, root: {root}, {self.pre_order_results}')

            self.preOrder(right_child, right_child_indices)

        return self.pre_order_results

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

def main():
    tree = TreeOrders()
    # print(tree.inOrder(tree.key[0]))
    print(tree.preOrder(tree.key[0]))
    # print(f'tree.results: {tree.results}')

    # print(" ".join(str(x) for x in tree.inOrder()))
    # print(" ".join(str(x) for x in tree.preOrder()))
    # print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

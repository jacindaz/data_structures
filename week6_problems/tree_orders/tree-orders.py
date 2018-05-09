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

        if root:
            left_child = self.key[self.left[root_index]]

            self.inOrder(left_child, self.left[root_index])
            self.results.append(root)

            right_child = self.key[self.right[root_index]]
            self.inOrder(right_child, self.right[root_index])

        return self.results

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

def main():
    tree = TreeOrders()
    print(tree.inOrder(tree.key[0]))
    # print(f'tree.results: {tree.results}')

    # print(" ".join(str(x) for x in tree.inOrder()))
    # print(" ".join(str(x) for x in tree.preOrder()))
    # print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

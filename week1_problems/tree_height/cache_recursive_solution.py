# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = self.n * [0]

    def path_length(self, child_index):
        parent_index = self.parent[child_index]

        # base case
        if parent_index == -1:
            return 1

        # if node found in cache, return
        if self.cache[child_index]:
            return self.cache[child_index]

        # otherwise, calculate using recursion from parent node
        self.cache[child_index] = 1 + self.path_length(parent_index)
        return self.cache[child_index]

    def compute_height(self):
        results = self.n * [0]
        for n in range(self.n):
            results[n] = self.path_length(n)

        return max(results)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

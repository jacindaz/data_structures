# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;

    def compute_height_with_print_statements(self):
        # Replace this code with a faster implementation
        print(f'-----------------')
        print(f'self.n: {self.n}, self.parent: {self.parent}')
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            print(f'-----------------')
            print(f'height: {height}, vertex: {vertex}, i: {i}')

            while i != -1:
                height += 1
                i = self.parent[i]
                print(f'height: {height}, i: {i}')
                print(f'self.parent: {self.parent}')

            maxHeight = max(maxHeight, height);
            print(f'maxHeight: {maxHeight}')

        return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_with_print_statements())

threading.Thread(target=main).start()

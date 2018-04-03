# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def build_tree(self):
        print(f'self.parent: {self.parent}')

        nodes = []
        for parent in self.parent:
            nodes.append({ 'parent': parent, 'children': [] })
        print(f'\nnodes: {nodes}\n')

        for child_index, parent_index in enumerate(self.parent):
            print('-------------------')
            print(f'child_index: {child_index}, parent_index: {parent_index}')
            if parent_index == -1:
                root = child_index
            else:
                nodes[parent_index]['children'].append(child_index)
                print('adding child to parent node')
                print(f'\nnodes: {nodes}\n')

    def compute_height(self):
        # Once you’ve built the tree, you’ll then need to compute its height.
        # If you don’t use recursion, you needn’t worry about stack overflow problems.
        # Without recursion, you’ll need some auxiliary data structure to keep
        # track of the current state (in the breadth-first seach code in lecture,
        # for example, we used a queue).

        # use breadth-first search
        # and a queue
        # to traverse the tree




def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()

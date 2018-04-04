# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

from collections import deque

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.tree = self.build_tree()

    def build_tree(self):
        print(f'self.parent: {self.parent}')

        nodes = {}
        for parent in self.parent:
            nodes[parent] = []
        print(f'\nnodes: {nodes}\n')

        for child_index, parent_index in enumerate(self.parent):
            print('-------------------')
            print(f'child_index: {child_index}, parent_index: {parent_index}')
            nodes[parent_index].append(child_index)

            print('adding child to parent node')
            print(f'\nnodes: {nodes}\n')
        return nodes

    def compute_height(self):
        # Once you’ve built the tree, you’ll then need to compute its height.
        # If you don’t use recursion, you needn’t worry about stack overflow problems.
        # Without recursion, you’ll need some auxiliary data structure to keep
        # track of the current state (in the breadth-first seach code in lecture,
        # for example, we used a queue).

        # use breadth-first search
        # and a queue
        # to traverse the tree
        #
        # Code from Lecture:
        # if tree = nil:
        #     return
        # queue = []
        # queue.enqueue(tree)
        # while not queue.empty():
        #     node = queue.dequeue()
        #     print(node)
        #     if node.left != nil:
        #         queue.enqueue(node.left)
        #     if node.right != nil:
        #         queue.enqueue(node.right)

        # self.tree
        # [
        #     {'parent': 4, 'children': []},
        #     {'parent': -1, 'children': [3, 4]},
        #     {'parent': 4, 'children': []},
        #     {'parent': 1, 'children': []},
        #     {'parent': 1, 'children': [0, 2]}
        # ]

        print(f'self.tree: {self.tree}')
        if len(self.tree) == 0:
            return 0
        else:
            queue = deque(self.tree)
            while len(queue) > 0:
                # get first node in tree
                node = queue.popleft()
                print(f'\nnode: {node}')
                print(f'queue: {queue}')


# Also, if you are performing many pop(0), you should look at collections.deque

# from collections import deque
# >>> l = deque(['a', 'b', 'c', 'd'])
# >>> l.popleft()
# 'a'
# >>> l
# deque(['b', 'c', 'd'])
# Provides higher performance popping from left end of the list



def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()

# test case
# 10
# 9 7 5 5 2 9 9 9 2 -1

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
        # print(f'self.parent: {self.parent}')

        nodes = {}
        for parent in self.parent:
            nodes[parent] = []
        # print(f'\nnodes: {nodes}\n')

        for child_index, parent_index in enumerate(self.parent):
            # print('-------------------')
            # print(f'child_index: {child_index}, parent_index: {parent_index}')
            nodes[parent_index].append(child_index)

            # print('adding child to parent node')
            # print(f'\nnodes: {nodes}\n')
        return nodes

    def compute_height(self):
        # Once you’ve built the tree, you’ll then need to compute its height.
        # If you don’t use recursion, you needn’t worry about stack overflow problems.
        # Without recursion, you’ll need some auxiliary data structure to keep
        # track of the current state (in the breadth-first seach code in lecture,
        # for example, we used a queue).

        # sorted tree
        # {-1: [9], 2: [4, 8], 5: [2, 3], 7: [1], 9: [0, 5, 6, 7]}

        sorted_tree = dict(sorted(self.tree.items()))
        queue = deque(sorted_tree)

        max_height = 0
        current_level = 1
        while len(queue) > 0:
            node = queue.popleft() # -1
            root_node = sorted_tree[node][0] # [9]
            root_node_children = sorted_tree[root_node]

            # [0, 5, 6, 7]
            children_queue = deque(root_node_children)
            while len(children_queue) > 0:
                # for node in root_node_children:
                node = children_queue.popleft()
                print('-----------------------------')
                print(f'root_node_children: {root_node_children}, children_queue: {children_queue}')
                print(f'current node: {node}, current_level: {current_level}')
                current_level += 1

                # start with 0
                # does 0 have any children?

                # if has children
                if node in sorted_tree:
                    children = sorted_tree[node]
                    print(f'\nnode ({node}) found, has children.')
                    print(f'children: {children}')

                    current_level += 1


                # if does not have children
                else:
                    print(f'\nnode ({node}) does not have any children.')
                    print('moving one level back up. ')
                    if current_level > max_height:
                        max_height = current_level
                    current_level -= 1



def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()

# test case
# 10
# 9 7 5 5 2 9 9 9 2 -1

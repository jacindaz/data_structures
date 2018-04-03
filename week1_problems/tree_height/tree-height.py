# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Suggestion: Take advantage of the fact that the labels
        # for each tree node are integers in the range 0..n-1:
        #  => you can store each node in an array whose index is the label of the node.
        #  => By storing the nodes in an array, you have O(1)
        #     access to any node given its label.

        # Create an array of n nodes:
        # allocate nodes[n]
        # for i=0 to n-1:
        #   nodes[i] = new Node
        # isn't self.parent already what this psuedocode is asking for???
        print(f'self.parent: {self.parent}')

        nodes = []
        # first add all the parents to the nodes
        for parent in self.parent:
            nodes.append({ 'parent': parent, 'children': [] })
        print(f'\nnodes: {nodes}\n')

        # then read each parent index:
        # for child_index=0 to n-1:
        #   read parent_index
        #   if parent_index == -1:
        #       root = child_index
        #   else:
        #       nodes[parent_index].addChild(nodes[child_index])

        # add children to nodes array
        for child_index, parent_index in enumerate(self.parent):
            print('-------------------')
            print(f'child_index: {child_index}, parent_index: {parent_index}')
            if parent_index == -1:
                root = child_index
            else:
                # first element: 0
                # parent_index is 4
                # so find parent node, which is at index 4
                # and add child to that node
                nodes[parent_index]['children'].append(child_index)
                print('adding child to parent node')
                print(f'\nnodes: {nodes}\n')





def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()

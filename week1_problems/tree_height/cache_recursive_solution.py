# import ipdb

class TreeHeight:
    def __init__(self, parents):
        self.parent = parents
        self.height_cache = len(self.parent) * [0]

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def store_heights_in_cache(self, top_down_heights, bottom_up_nodes):
        root_to_leaf = list(reversed(bottom_up_nodes))
        for index, node in enumerate(root_to_leaf):
            self.height_cache[node] = top_down_heights[index]

        return self.height_cache

    def path_length(self, child_index, parent_index):
        done = False
        height = 1 # start with 0, or 1?

        bottom_up_nodes = [child_index]
        top_down_heights = [1]
        while not done:
            # print('---------------')
            # print(f'child_index: {child_index}, parent_index: {parent_index}, height: {height}')
            # print(f'self.height_cache: {self.height_cache}')

            parent = self.parent[child_index]
            # print(f'parent: {parent}')

            if parent == -1:
                done = True
                break
            else:
                if self.height_cache[parent]:
                    # print('\nnice! height already in height cache')

                    # new height is the parent's height + 1
                    child_height = self.height_cache[parent] + 1
                    # print(f'child_height: {child_height}')

                    # append this child node's height to height cache
                    self.height_cache[child_index] = child_height
                    # print(f'self.height_cache: {self.height_cache}')

                    # print(f'\nself.height_cache before updates: {self.height_cache}')
                    self.store_heights_in_cache(top_down_heights, bottom_up_nodes)
                    # print(f'self.height_cache AFTER updates: {self.height_cache}\n')

                    # return child_height

                child_index = parent
                height += 1

            top_down_heights.append(height)
            bottom_up_nodes.append(parent)

            # print(f'\ntop_down_heights: {top_down_heights}')
            # print(f'bottom_up_nodes: {bottom_up_nodes}')
            # print('---------------')

        # print(f'\nself.height_cache before updates: {self.height_cache}')
        self.store_heights_in_cache(top_down_heights, bottom_up_nodes)
        # print(f'self.height_cache AFTER updates: {self.height_cache}\n')
        return height

    def tree_max_height(self):
        max_height = 0
        for child_index, parent_index in enumerate(self.parent):
            if parent_index == -1:
                next

            if self.height_cache[child_index] != 0:
                height = self.height_cache[child_index]

            else:
                self.path_length(child_index, parent_index)
                height = self.height_cache[child_index]

            if height > max_height:
                max_height = height

        # print(f'\nFINAL self.height_cache: {self.height_cache}\n')
        return max_height

# parents = [9,7,5,5,2,9,9,9,2,-1,4] # 5
# tree = TreeHeight(parents)
# print(tree.path_length(4,2))

# parents = [-1,0,4,0,3] # 4
# parents = [4,-1,4,1,1] # 3
parents = [9,7,5,5,2,9,9,9,2,-1] # 4
# parents = [9,7,5,5,2,9,9,9,2,-1,4] # 5

# BOUNDARY CASES
# parents = [-1] # 1
# parents = [-1, 0] # 2
# parents = [-1,0,1,2,3,4,5,6,7,8] # 10

# max: 100000
def max_height_tree(max):
    nodes = [-1]
    for n in range(0,max-1):
        nodes.append(n)

    return nodes

# STRESS TEST

# tree = TreeHeight(max_height_tree(500))

# parents = [9,7,5,5,2,9,9,9,2,-1,4]
# tree = TreeHeight(parents)
print(tree.tree_max_height())
# max_height: 5
# height_cache: [2,3,3,3,4,2,2,2,4,1,5]

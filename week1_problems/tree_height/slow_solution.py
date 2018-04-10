class TreeHeight:
    def __init__(self, parents):
        self.parent = parents

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def path_length(self, node_id):
        done = False
        height = 1
        while not done:
            parent = self.parent[node_id]
            if parent == -1:
                done = True
            else:
                node_id = parent
                height += 1
        return height

    def tree_max_height(self):
        cache = []
        for index, node in enumerate(self.parent):
            height = self.path_length(index)
            cache.append(height)
        return max(cache)


# parents = [-1,0,4,0,3] # 4
# parents = [4,-1,4,1,1] # 3
# parents = [9,7,5,5,2,9,9,9,2,-1] # 4
parents = [9,7,5,5,2,9,9,9,2,-1,4] # 5

# BOUNDARY CASES
# parents = [-1] # 1
# parents = [-1, 0] # 2
# parents = [-1,0,1,2,3,4,5,6,7,8] # 10

# max: 100000
def max_height_tree(max):
    nodes = [-1]
    for n in range(0,max):
        nodes.append(n)

    return nodes

# STRESS TEST

# tree = TreeHeight(max_height_tree(100000))
tree = TreeHeight(parents)
print(tree.tree_max_height())

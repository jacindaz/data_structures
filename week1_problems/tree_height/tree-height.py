def path_length(node_id):
    done = False
    height = 1
    while not done:
        parent = parents[node_id]
        # print('----------------')
        # print(f'parent: {parent}, node_id: {node_id}')
        # print(f'height: {height}')

        if parent == -1:
            done = True
        else:
            node_id = parent
            height += 1
    return height

# 10
# 9 7 5 5 2 9 9 9 2 -1
# print(path_length(8)) # 4
# print(path_length(0)) # 2
# print(path_length(9)) # 1


def tree_max_height(tree):
    # SIMPLEST SOLUTION FIRST
    cache = []
    for index, node in enumerate(tree):
        # find the height of the node
        height = path_length(index)

        # store it in the cache
        cache.append(height)

    print(f'cache: {cache}')
    # find the max value
    return max(cache)

# parents = [9,7,5,5,2,9,9,9,2,-1]
# parents = [-1,0,4,0,3]
parents = [4,-1,4,1,1]
print(tree_max_height(parents))

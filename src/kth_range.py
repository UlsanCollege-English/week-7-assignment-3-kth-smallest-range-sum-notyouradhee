class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    # TODO: return new root after insert (reject duplicates)
    if root is None:
        return Node(key)

    node = root
    parent = None
    while node is not None:
        parent = node
        if key < node.key:
            node = node.left
        elif key > node.key:
            node = node.right
        else:
            # duplicate, reject
            return root

    if key < parent.key:
        parent.left = Node(key)
    else:
        parent.right = Node(key)

    return root

def kth_smallest(root, k):
    # TODO
    if k < 1:
        raise IndexError('k is out of bounds')

    stack = []
    node = root
    count = 0

    while stack or node:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        count += 1
        if count == k:
            return node.key

        node = node.right

    raise IndexError('k is out of bounds')

def range_sum_bst(root, low, high):
    # TODO
    if root is None:
        return 0

    if root.key < low:
        return range_sum_bst(root.right, low, high)

    if root.key > high:
        return range_sum_bst(root.left, low, high)

    return root.key + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

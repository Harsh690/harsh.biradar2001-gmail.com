from collections import OrderedDict


def getLevelUtil(node, data, level):
    if (node == None):
        return 0

    if (node.data == data):
        return level

    downlevel = getLevelUtil(node.left,
                             data, level + 1)
    if (downlevel != 0):
        return downlevel

    downlevel = getLevelUtil(node.right,
                             data, level + 1)
    return downlevel


# Returns level of given data value


def getLevel(node, data):
    return getLevelUtil(node, data, 1)


def pathCounts(root):
    val = dict()
    if root is None:
        return
    res = []
    stack = []
    stack.append(root)
    node_val = stack[0]
    while len(stack) > 0:

        node = stack.pop()
        res.append(node.data)

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

        if node.right is None and node.left is None:
            flag = getLevel(node_val, node.data)
            if flag in val:
                val[flag] += 1
            else:
                val[flag] = 1

    for key, values in val.items():
        print(key, values, end=" $")
    return
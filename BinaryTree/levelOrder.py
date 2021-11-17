## Given the root of a binary tree, return the level order traversal of its nodes' values

def levelOrder1(root): # O(n), iterative
    if not root:
        return []
    
    current = [root]
    res = [[root.val]]

    while len(current) > 0:
        temp = []
        for node in current:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        if len(temp)>0:
            res.append([i.val for i in temp])
        current = temp

    return res
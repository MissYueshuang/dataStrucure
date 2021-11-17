def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    if not root:
        return 0
    else:
        depth = 1

    return depth + max(maxDepth(root.left), maxDepth(root.right))
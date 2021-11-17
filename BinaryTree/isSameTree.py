def isSameTree(p, q) -> bool:
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    elif not p or not q:
        return False
    
    if p.val == q.val: 
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else:
        return False



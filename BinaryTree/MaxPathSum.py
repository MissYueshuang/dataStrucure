# find the max path sum
def MaxPathSum1(root): # recursive
    if not root:
        return 0

    return root.val + max(MaxPathSum1(root.left), MaxPathSum1(root.right))
def mirrorTree(root):
    if root:
        temp = mirrorTree(root.left)
        root.left = mirrorTree(root.right)
        root.right = temp

    return root
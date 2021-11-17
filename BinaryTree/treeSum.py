## Get the sum of the whole tree
def treeSum1(root): # recursive
    if not root:
        return 0
    
    return root.val + treeSum1(root.left) + treeSum1(root.right)

# treeSum1(a)

def treeSum2(root): # iterative for depth-first-values
    if not root:
        return 0
    
    stack = [root]
    res = 0

    while len(stack)>0:
        current = stack.pop()
        res += current.val
        print(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)        
    
    return res

# treeSum2(a)

def treeSum3(root): # iterative for breadth-first-values
    if not root:
        return 0
    
    queue = [root]
    res = 0

    while len(queue)>0:
        current = queue[0]
        queue = queue[1:]
        
        print(current.val)
        res += current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return res

# treeSum3(a)
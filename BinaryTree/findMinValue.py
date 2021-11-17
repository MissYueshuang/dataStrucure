## find min value
def findMinValue1(root): # recursive
    if not root:
        return float('inf')
    leftMin = findMinValue1(root.left)
    rightMin = findMinValue1(root.right)

    return min(root.val, leftMin, rightMin)


def findMinValue2(root): # iterative
    if not root:
        return float('inf')
    
    smallest = float('inf')
    stack = [root]

    while len(stack)>0:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return smallest   

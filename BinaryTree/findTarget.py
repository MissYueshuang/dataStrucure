## findTargetValue
def findTarget(root,target):
    if not root:
        return False
        
    if root.val == target:
        return True
    if findTarget(root.left,target) | findTarget(root.right,target):
        return True
    else:
        return False
            
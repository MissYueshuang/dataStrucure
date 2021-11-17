"""
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.
"""
from BinaryTree.treeNode import Node

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return None

    midIdx = len(nums)//2
    
    root = Node(nums[midIdx])

    left = nums[:midIdx]
    right = nums[midIdx+1:]
    
    root.left = sortedArrayToBST(left)        
    root.right = sortedArrayToBST(right)

    return root

# res = sortedArrayToBST(nums)
# nums = [-10,-3,0,5,9]
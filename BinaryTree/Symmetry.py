class Symmetry:
    def isSymmetric(self,root) -> bool:
            if root:
                return self.__is_symmetric(root.left, root.right)
            else:
                return True
            
    def __is_symmetric(self,left, right) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return self.__is_symmetric(left.right, right.left) and self.__is_symmetric(left.left, right.right) and right.val == left.val 

# def isSymmArr(arr):
#     arr = [i.val if i is not None else None for i in arr]
#     if len(arr)==1:
#         return True
#     mid = len(arr)//2
#     if arr[:mid] == arr[mid:][::-1]:
#         return True
#     else:
#         return False

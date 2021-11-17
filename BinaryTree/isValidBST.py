# Check if is A valid BST 
class validBST:
    def leftLast(self,node):
        while node.left:
            node = node.left
        return node.val
        
    def rightLast(self,node):
        while node.right:
            node = node.right
        return node.val

    def isValidBST(self,root):
        stack = [root]
        res = True

        while len(stack)>0 and res:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
                res = res and current.val < self.leftLast(current.right) # (left min)
                
            if current.left:
                stack.append(current.left)
                res = res and current.val > self.rightLast(current.left)  # right max 
            
        return res
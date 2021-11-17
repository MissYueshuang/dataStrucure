# their distance happened to be 2: mostrightIndex - mostLeftIndex + 1
def widthOfBinaryTree(root) -> int:
    max_width = 0
    q = [(root,0)] # store root and index pair in a queue
    while q:
        length = len(q)
        max_width = max(max_width, q[-1][1] - q[0][1] + 1)
        for _ in range(length):
            node, idx = q[0]
            q = q[1:]
            if node.left:
                q.append((node.left, 2 * idx))
            if node.right:
                q.append((node.right, 2 * idx + 1))
                
    return max_width

# Version_1
def MaxWidth(root):
    if not root:
        return False
    
    current = [root]
    res = [[root]]

    while len(current) > 0:
        temp = []
        if any(current):
            for node in current:
                if node is not None:
                    temp.append(node.left)
                    temp.append(node.right)
                else: 
                    temp.append(None)
                    temp.append(None)              
            if any(temp):
                while temp[0] is None: # delete NOne before 
                    temp = temp[1:]        
                while temp[-1] is None: # delete None in the end
                    temp = temp[:-1]
                res.append([i for i in temp])
                current = temp
            else: 
                break   

    return max([len(i) for i in res])

# # the Width of tree
# def treeWidth(root): # O(n), iterative
#     if not root:
#         return []
    
#     res = []
#     queue = [[root]]

#     while len(queue[0]) > 0:
#         current = queue[0]
#         queue = queue[1:]

#         res.append(current)            
        
#         temp = []
#         for i in current:
#             if i.left:
#                 temp.append(i.left)
#             if i.right:
#                 temp.append(i.right)

#         queue.append(temp)

#     return max([len(i) for i in res])
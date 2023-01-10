def getAllElements(root1,root2):   
        def dfs(root):
            if root is None:
                return []
            visited=[]
            stack=[root]
            while(stack):
                temp = stack.pop()
                if temp.right is not None:
                    stack.append(temp.right)
                if temp.left is not None:
                    stack.append(temp.left)
                visited.append(temp.val)
            return visited
        l1=dfs(root1)+dfs(root2)
        l1.sort()
        return l1
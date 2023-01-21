from functools import cache
@cache
def rob(self, root, canRob = True):
        if not root: return 0
        dont_rob = self.rob(root.left, True) + self.rob(root.right, True)
        if canRob:
            rob_root = root.val + self.rob(root.left, False) + self.rob(root.right, False)
        else: 
            rob_root= -1
        return max(dont_rob, rob_root)
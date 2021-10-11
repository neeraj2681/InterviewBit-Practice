# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    lister = []
    pos = -1
    
    def left_appender(self, root):
        while (root != None):
            self.lister.append(root)
            root = root.left
            self.pos+=1
            
    def __init__(self, root):
        self.pos = -1
        self.lister = []
        self.left_appender(root)
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if (self.pos >= 0):
            return True
        return False
        
    # @return an integer, the next smallest number
    def next(self):
        temp = None
        if (self.pos >= 0):
            temp = self.lister[self.pos]
            self.lister.pop(self.pos)
            self.pos-=1
        self.left_appender(temp.right)
        return temp.val
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

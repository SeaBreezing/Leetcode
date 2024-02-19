# https://leetcode.cn/problems/binary-tree-preorder-traversal/
# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# https://leetcode.cn/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: # 如果遍历到了空，则归
            return []
        left = self.preorderTraversal(root.left) # 更换相应函数
        right = self.preorderTraversal(root.right)
        # 前序
        return  [root.val] + left +  right # list相加
        # 中序
        # return left + [root.val] +right
        # 后序
        # return left+right+[root.val]

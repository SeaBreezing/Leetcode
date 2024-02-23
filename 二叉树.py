# 前中后序遍历
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

#【102】层序遍历
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        # 空判定
        if not root:
            return []
        # 把树压平到队列中, 注意root要放在列表里，因为参数要是iterable
        # 一定注意，queue存的是节点（子树），不是值
        queue = collections.deque([root])
        # 用于存放结果的二维列表
        result = []
        # queue非空时，因为会不断往queue里面放下一层的元素
        while(queue):
            level = [] # 用于存放当前层的元素，每层结束后拼接到result上去
            for i in range(len(queue)):
                cur = queue.popleft() # 此时
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left) # 不是.val
                if cur.right:
                    queue.append(cur.right) # 不是.val
            result.append(level)
        return result

#【翻转二叉树】
# https://leetcode.cn/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def swap(self, a, b):
        tmp = a
        a = b
        b = tmp
        return a, b
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.swap(root.left, root.right)
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root

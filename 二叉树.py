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

#【翻转二叉树】递归法，我没有写层序遍历的方法
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
        # 注意，写前序和后序都可以，中序不是这个逻辑。如果按这个逻辑写中序，永远只能遍历一个子树，根节点的另一个子树遍历不到。画一下就知道了
        # 遍历只是流程，在不断的遍历中做翻转的操作
        root.left, root.right = self.swap(root.left, root.right)
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root

#【对称二叉树】递归
# https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-100-liked
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 不是左右子树相同，是对称
        i = 0

        def isSame(p, q):
            # p and q are two TreeNodes to be compared
            # p和q是两个子树
            if (p is None or q is None):
                return p is q    
            return ((p.val == q.val) and isSame(p.left, q.right) and isSame(p.right, q.left))
        
        return isSame(root.left, root.right)
#【平衡二叉树】递归
# https://leetcode.cn/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 问题：
        # 根 左右 如何是平衡 关注小局部
        # 左 是
        # 右 是
        # 左右 高度 绝对值 <= 1
        height, flag = 0, 1
        flag, height = self.sub_is(root, flag, height)
        if(flag == -1):
            return False
        else:
            return True

    def sub_is(self, root, flag, height):
        if root is None:
            return flag, height
        flag, lefth = self.sub_is(root.left, flag, height)
        if flag == -1:
            return flag, height
        flag, righth = self.sub_is(root.right, flag, height)
        if flag == -1 or abs(lefth - righth) > 1:
            flag = -1
            return flag, height
        height = max(lefth, righth) + 1
        return flag, height

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
        if flag == -1: # 左子树不平衡
            return flag, height
        flag, righth = self.sub_is(root.right, flag, height)
        if flag == -1 or abs(lefth - righth) > 1: # 右子树不平衡 或 左右差>1（这里逻辑上是两件事，为了代表简洁合在一起写了）
            flag = -1
            return flag, height
        height = max(lefth, righth) + 1 # 这里加的1是当前层的1，不然最后就是0+0+0+...
        return flag, height

#【二叉树右视图】
# https://leetcode.cn/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-100-liked
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# 对于递归来说，返回值和参数不一定要一样？
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 先遍历右子树，再遍历左子树，左子树中深度（把深度记下来）大于结果列表长度，才记入结果
        ans = []
        def dfs(root, depth):
            if root is None:
                return
            if depth == len(ans):
                ans.append(root.val)
            dfs(root.right, depth+1) # 先遍历右子树
            dfs(root.left, depth+1)
        dfs(root, 0)
        return ans
        
#【完全二叉树的节点个数】
# https://leetcode.cn/problems/count-complete-tree-nodes/
class Solution:
    # 分解为子问题：左子树+右子树+1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left)+self.countNodes(root.right) + 1
        
#【判定二叉搜索树】先得到当前节点值，再分别往左往右，这是前序遍历
# https://leetcode.cn/problems/validate-binary-search-tree/description/
class Solution:
    # 方法一：中序遍历，存入一个数组，数组单调递增，则True
    # 方法二：前序遍历（本题解）。误区：不是根节点比与左右节点比较，而是与左右子树比较
    # 方法三：返回左右子树的最大最小值（都要），再与中间的根节点比较，再如此递归，这是后序遍历
    # 往当前节点的左子树遍历时，对左区间没有要求(-inf), 右区间要求是当前节点值
    # 往当前节点的右子树遍历时，对右区间没有要求(-inf), 左区间要求是当前节点值
    # 注意，递归嵌套时，区间是不断向下传递的，比如遍历右子树(1)的左子树(2)
    # 虽然第(2)步独立看对左区间没有要求，但传递了第(1)步对左子树的要求，递归时参数也得到了传递
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root, left=-inf, right=inf):
            if root is None:
                return True
            x = root.val # 首先要获得当前节点值
            if root is None: # 递归的边界条件，即空节点
                return True
            judge = left < root.val < right
            return judge and isBST(root.left, left, x) and isBST(root.right, x, right) # 左子树
        return isBST(root)

#【二叉树的直径】贪心，慢
# https://leetcode.cn/problems/diameter-of-binary-tree/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    # maxd = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 子树的子树可能非常复杂，直径不一定经过了根节点
        # 当前节点代表的树的直径=左子树深度+右子树深度
        # 还需要一个后序遍历，每个子树都要走到（贪心）
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right))+1
        if root is None:
            return 0    
        lefth = height(root.left) # 注意是左子树，不包括根节点，不要自己验证反而验证错了
        righth = height(root.right)
        print(f'lefth:{lefth}')
        print(f'righth:{righth}')
        diameter = lefth + righth
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), diameter)  

#【从中序与后序遍历序列构造二叉树】很慢，打印的输出有助于理解递归
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 用后序的最后一个切割中序，将中序分为左子树和右子树
        # 如何从后序中找到中序：切割的子段和中序被分割后的子段大小相同，且后序按照左右中遍历
        # 递归
        if inorder == []:
            return
        # 用后序的最后一个切割中序
        root = TreeNode(postorder[-1])
        print(f'root1:{root}')
        root_left, root_right = [], []
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_left = inorder[:i]# 数组, 第i+1个元素前的i个都放入root_left
                root_right = inorder[(i+1):] # 从索引i+1开始，中间那个是节点
        # 用切割后的中序找后序
        post_left = postorder[:len(root_left)]
        post_right = postorder[(len(root_left)):(len(root_left)+len(root_right))]
        root.left = self.buildTree(root_left, post_left) # 用后序的最后一个切割中序后，得到的两个子树分开处理即可，先后不重要
        root.right = self.buildTree(root_right, post_right)
        print(f'root2:{root}')
        return root



# ACM模式 使用前序和中序遍历构造二叉树，并使用后序遍历打印出来
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    left_inorder = inorder[:inorder.index(root_val)]
    right_inorder = inorder[inorder.index(root_val)+1:]
    left_preorder = preorder[1:len(left_inorder) + 1]
    right_preorder = preorder[len(left_inorder) + 1:]

    root = Node(root_val)
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)
    return root

def postorder_travel(root):
    if not root:
        return []
    left = postorder_travel(root.left)
    right = postorder_travel(root.right)
    return left + right + [root.val]
    
preorder, inorder = map(str, input().split())
root = build_tree(preorder, inorder)
postorder = postorder_travel(root)
print(''.join(postorder)) # 将列表中所有元素串起来，分隔符为引号内的东西（此处即没有分隔符）

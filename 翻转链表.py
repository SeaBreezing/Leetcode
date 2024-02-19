# https://leetcode.cn/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None # 虚头指针
        cur = head
        while(cur != None):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

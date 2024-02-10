# 原地反转字符串
# 
# 方法一
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        while(left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        s = str(s)
        return(s)

# 方法二
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = list(s)
        length = len(s)
        for i in range(length // 2):
            s[i], s[length-1-i] = s[length-1-i], s[i]
        s = str(s)
        return(s)

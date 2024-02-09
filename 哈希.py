# 有效的字母异位词
# https://leetcode.cn/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0]*26
        for i in s:
            record[ord(i)-ord('a')]+=1
        for i in t:
            record[ord(i)-ord('a')]-=1
        for i in range(len(record)):
            if(record[i] != 0):
                return False
        return True

# 快乐数
# https://leetcode.cn/problems/happy-number/
class Solution(object):
    def cal(self, n):
        result = 0
        if (n > 10):
            while(n//10):# 取余数
                result += (n % 10)**2
                print(f'result={result}')
                n = n//10 # 地板除
        result += n ** 2
        return result
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 如果集合中出现了这个数，那么会进入无限循环，该数不是快乐数
        record = set() # create a set
        if n <= 0:
            return False
        while(n != 1):
            n = self.cal(n)
            if n in record:
                return False
            else:
                record.add(n)
        return True


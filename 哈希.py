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


# 两数之和
# https://leetcode.cn/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        # 遍历数组，当target-nums[i]在dict的key中存在，则返回value(下标)
        # 否则将nums[i]及其下标存入dict
        # j -> int, i -> index
        rec = {} # 创建一个hashtable
        for i in range(len(nums)):
            j = target - nums[i]
            if j in rec.keys():
            # if rec.has_key(j): # 更快，但python3删掉了
                return i, rec[j] # 返回i和j在nums中对应的数组下标
            else:
                rec[nums[i]] = i

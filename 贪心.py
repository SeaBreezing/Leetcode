# 局部最优推出全局最优，并举不出反例，那么试试贪心！
# 分发饼干
# https://leetcode.cn/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: 胃口   s: 饼干
        # 越大的饼干给越大胃口的孩子，这样才能（举不出反例）尽可能不造成浪费
        # 先排序！！
        g.sort()
        s.sort()
        if len(s) == 0:
            return 0
        sj = len(s) - 1
        result = 0
        for i in range(len(g)-1, -1, -1): 
        # for 用来遍胃口，这样指向饼干的指针才能移动，因为如果胃口最大的孩子无法满足，总有胃口小的孩子能被满足
        # 否则，遍历饼干时，一旦胃口最大的孩子不能被满足，两个指针都没办法移动（指向胃口的指针，因为不满足if条件，无法移动）
            if sj < 0:
                break
            print(f'胃口:{g[i]}, 饼干:{s[sj]}')
            if s[sj] >= g[i]:
                sj -= 1
                result += 1
        return result

# 最大子数组和
# https://leetcode.cn/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        count = 0
    
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            # 注意，先更新还是先清零的位置很重要。如果全为nums全为-1，需要有-1>-inf更新result
            # 而，清零的只是当前和，并不是被更新的结果
            if count < 0: # 即当前和是负数，对最终结果只会有不好的影响
                count = 0 # 直接将结果清零 贪心就是这里

    
        return result
        
        

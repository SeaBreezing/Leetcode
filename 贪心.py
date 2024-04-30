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
# 贪心的思路为局部最优（当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小）从而推出全局最优（选取最大“连续和”）
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
        
# 跳跃游戏        
# https://leetcode.cn/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        cur = 0
        while cur <= cover: # python允许while循环的边界变化 for 循环不允许
            cover = max(cover, cur + nums[cur])
            cur += 1
            if cover >= len(nums) - 1:
                return True
        return False

# 划分字母区间
# https://leetcode.cn/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, s):

        # 1. 得到每个字母的最大出现下标
        per_max = {}
        for st in range(len(s)):
            if s[st] in per_max.keys():
                if st > per_max[s[st]]:
                    per_max[s[st]] = st
            else:
                per_max.update({s[st]: st})
        print(per_max)

        
        # 2. 在从当前起始点（比如切割点的下一个下标）进行到『暂时切割点』时，过程中会被迫碰到一些字母，如果这些字母出现的最大下标大于『暂时切割点』，需要延长『暂时切割点』
        # 注意 idx += 1 的写法
        cut_index = []
        start = s[0]
        idx = 0
        cut_idx_tmp = per_max[start]
        
        while idx < len(s):
            while idx <= cut_idx_tmp:
                print(f'当前字母最大下标处：{per_max[s[idx]]}, tmp切割: {cut_idx_tmp}, {s[idx]}')
                if per_max[s[idx]] > cut_idx_tmp:
                    cut_idx_tmp = per_max[s[idx]]
                if idx == cut_idx_tmp:
                    cut_index.append(cut_idx_tmp)
                idx += 1
            print(f'idx:{idx}, cut_idx_tmp:{cut_idx_tmp}')
            if idx < len(s):
                cut_idx_tmp = per_max[s[idx]]
        
        print(cut_index)
        cut_len = [cut_index[0] + 1]
        cut_len.extend([cut_index[i+1] - cut_index[i] for i in range(len(cut_index) - 1)])
        
        return cut_len

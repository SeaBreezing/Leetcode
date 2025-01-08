#【移动零】
# https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        rec = 0
        for i in range(len(nums)):
            if (nums[i]!=0):
                nums[slow] = nums[i]
                slow += 1
        print(nums)
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums
            
#【乘水最多的容器】
# https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        vol_max = 0
        # 如向内移动长板，水量一定减少，则因此要找最大值，只需要移短板
        while(end>start):
            vol = (end-start) * min(height[end], height[start])
            vol_max = vol if vol > vol_max else vol_max
            if(height[end] > height[start]):
                start += 1
            else:
                end -= 1
        return vol_max

#【三数之和】
# https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-100-liked
# 简洁无注释版
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         result = []
#         for i in range(len(nums)):
#             if (i > 0 and nums[i] == nums[i-1]): # 这里i>0很重要，容易忘
#                 continue
#             left = i+1
#             right = len(nums)-1
#             while(left < right):
#                 if(nums[i]+nums[left]+nums[right]<0):
#                     left += 1
#                     continue
#                 elif(nums[i]+nums[left]+nums[right]>0):
#                     right -= 1
#                     continue
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])
#                     while(left < right and nums[left] == nums[left+1]):
#                         left += 1
#                     while(left < right and nums[right] == nums[right-1]):
#                         right -= 1
#                     left += 1
#                     right -= 1
#         return result

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            # ---------去重
            if(i > 0 and nums[i] == nums[i-1]): # nums[-1]是有定义的，[0, 0, 0]的时候会直接continue
                continue
            # ---------
            left = i+1
            right = len(nums) - 1
            while(right>left):
                # 双指针，两个指针不是一起变的，而是根据逻辑，变哪个才有意义
                if(nums[i] + nums[left]+nums[right] <0):
                    left += 1
                elif(nums[i] + nums[left]+nums[right] >0): #而非if, 因为上面if一执行，left一变，这里条件可能就不是我原意了
                    right -= 1
                else:# ==0
                    # 先append再去重：后面去重的逻辑非常方便去重，基于这种去重逻辑才有了先append
                    result.append([nums[i], nums[left], nums[right]]) # 添加上一个列表（一个元素），只能用append
                    # ---------去重
                    # ！！！是while，不是if！！！
                    # while的逻辑很好理解，如果重复了，就一直移动这个指针，移出重复区域（前提是列表排过序了）
                    # 如果是if-continue，就是continue了又append，实际上没有去重
                    while(left < right and nums[left] == nums[left+1]): # left < right, 否则找着找着left就出去了
                        left += 1
                        # continue
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                        # continue
                    # ---------
                    left += 1
                    right -= 1 # 找到答案时，双指针同时收缩，因为只收缩一个肯定不是答案
                    print(f'left:{left}')
                    print(f'right:{right}')


                # print(result)
        return result

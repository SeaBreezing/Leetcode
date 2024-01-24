//二分查找
//https://leetcode.cn/problems/binary-search/
class Solution {
    public int search(int[] nums, int target) {
        int len = nums.length;
        int left = 0;
        int right = len - 1; //注意不是len/2，也不是len，而是len-1
        if (target < nums[0] | target > nums[len-1]){
            return -1;
        }//可以直接判断的情况
        while(left <= right){
            int middle = left + (right - left) / 2;//相比(left+right)/2可以防止溢出
            if (target < nums[middle]){
                right = middle - 1; // middle肯定不是了，因此要middle-1
            }
            else if(target > nums[middle]){
                left = middle + 1; //同上
            }
            else if(target == nums[middle])
                return middle;            
        }
        return -1;//在[nums[0], nums[len-1]]之间，但不是已有的数
    }
}


//删除指定元素【双指针】
//https://leetcode.cn/problems/remove-element/
class Solution {
    public int removeElement(int[] nums, int val) {
        int slowIndex = 0, fastIndex = 0;
        for(fastIndex = 0; fastIndex < nums.length; fastIndex++){
            if (nums[fastIndex] != val){
                nums[slowIndex] = nums[fastIndex]; //只是覆盖，数组长度没有变
                slowIndex++;
                //可以简写成nums[slowIndex++] = nums[fastIndex];
                //eg. 对[8, 10, 3, 12, 17, 3, 5], val=3
                //fast 原数组   8 10  3 12 17 3 5 
                //slow 新数组   8  3 12 17  5
                //这样手写下来，即只要nums[fastIndex]!=val, 就在新数组相同索引的地方复制
                //如果nums[fastIndex]==val, 新数组这个地方就不复制, 即指针slowIndex不移动
           }
        }
        return slowIndex;
    }
}

//有序数组的平方【双指针】
//https://leetcode.cn/problems/squares-of-a-sorted-array/
class Solution {
    public int[] sortedSquares(int[] nums) {
    //如果直接取绝对值再排序，最优的排序算法时间复杂度是nlogn, 太大了
    int[] result = new int [nums.length];
    int i = 0, j = nums.length-1, k = nums.length-1;
    while(i <= j){ //注意是<=, 且是while, 不要写成fori了, i不应该每次迭代都动, 而是满足if才会动
        if(nums[i] * nums[i] > nums[j] * nums[j]){
            result[k--] = nums[i] * nums[i];
            i++;
        }
        else{
            result[k--] = nums[j] * nums[j];
            j--;
        }
    }
    return result; 
    }
}

// 长度最小的子数组【滑动窗口】
// https://leetcode.cn/problems/minimum-size-subarray-sum/
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int result = Integer.MAX_VALUE; // 返回值
        // 遇到子数组问题，优先想滑窗
        // 对于for循环，每次迭代的是滑窗的终止索引还是起始索引？
        // 如果是起始索引，还是变成了暴力搜索，所以forj应该for的是终止索引
        // O(n): 对于每个元素，进滑窗的时候算一次（sum+=），出滑窗的时候再算一次（减sum-=）
        int sum = 0, i = 0, sublength = 0;
        for(int j = 0; j < nums.length; j++){
            sum += nums[j];
            // 精华在下面这个while循环，即滑窗的起始索引如何变化
            while (sum >= target){ // 而不是if, 因为终止位置不变时，起始位置要不断变化，直至滑窗内sum<s
                              // 而非终止位置每移动一次，起始位置最多只需要变一次
                sublength = j - i + 1;
                sum -= nums[i++];
                result = Math.min(result, sublength); // 相当于每个符合条件的滑窗都看过一次了，最后保存的是最小长度
            }
        }
        if (result == Integer.MAX_VALUE)
            return 0;
        else return result;
    }
}

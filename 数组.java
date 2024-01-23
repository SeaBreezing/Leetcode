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


//删除指定元素
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

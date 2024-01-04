# Leetcode
#### 时间复杂度
n是数据规模（比如n次循环，数组长度为n），代码中执行次数最多的语句，其执行的次数就是时间复杂度。如果for循环设置的稍微复杂一点，设执行次数为x，归纳法，一直到截止条件，解方程<br>
如果执行次数跟数据规模没有关系，就算O(1)<br>
log(n)：就像二分查找，每次执行，元素个数减半，这种很可能复杂度是log(n)<br>
#### coding技巧
1. 模块化，比如需要初始化一个矩阵，先假设有这样一个函数，稍后有时间再写完，而不是花时间写初始化的代码<br>
2. 错误检查，写TODO
3. 白板编程下，先理清思路再写
4. 白板测试，for循环尤其注意初始化的地方
5. 平时记下自己经常犯错的热点，递归中的基线条件、整数除法、二叉树中的空节点、链表迭代中的开始和结束，这些要反复检查才行
6. 短小精悍的用例，而非大而全的用例
7. 空值、单个元素、极端情况
8. 发现bug后仔细斟酌，找出最佳的修改方案
9. 蛮力法优先，然后再想B(时间复杂度最大的地方)UD优化策略

## 数据结构
### 链表
不擅长随机访问和排序
### 二叉树
尤其擅长排序

# n = int(input())
# m = list(map(int, input().split()))
# x = list(map(int, input().split()))
# result = {0}
# amount = []
# for i in range(n):
#     for j in range(x[i]):
#         amount.append(m[i])
# for i in amount:
#     for j in list(result):
#         result.add(i + j)
# print(len(result))

# input_list = input().split(";")
# initial = [0, 0]
# for item in input_list:
#     if not 2 <= len(item) <= 3:
#         continue # 如果满足，就继续下一个循环
#     try:
#         direction = item[0]
#         step = int(item[1:])
#         if direction in ["A", 'S', 'W', 'D']:
#             if direction == 'A':
#                 initial[0] -= step
#             elif direction == 'D':
#                 initial[0] += step
#             elif direction == 'S':
#                 initial[1] -= step
#             elif direction == 'W':
#                 initial[1] += step
#     except:
#         continue
# print(str(initial[0]) + ',' + str(initial[1]))



a = input().split(".")
flag = 1
if len(a) != 4:
    flag = 0
    print('NO')
else:
    for sub in a:
        if len(sub) > 3:
            print('NO')
            flag = 0
            break
        if not sub.isdigit(): # 如果字符串中有任何一个字符不是数字
            print('NO')
            flag = 0
            break
        if (sub[0] == '0' and len(sub) != 1):
            print('NO')
            flag = 0
            break
        if int(sub) > 255:
            print('NO')
            flag = 0
            break
if flag == 1:
    print('YES')






s = "ababcbacadefegdehijhklij"


def partitionLabels(s: str):
    # 1. 先找出所有字母出现的最大下标
    per_max = {}
    for st in range(len(s)):
        if s[st] in per_max.keys():
            if st > per_max[s[st]]:
                per_max[s[st]] = st
        else:
            per_max.update({s[st]: st})
    print(per_max)

    
    # 2. 
    part_index = []
    
    while i < 

             


















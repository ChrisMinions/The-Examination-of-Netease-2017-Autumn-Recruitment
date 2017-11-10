'''
[编程题] 跳石板
时间限制：1秒
空间限制：32768K
小易来到了一条石板路前，每块石板上从1挨着编号为：1、2、3.......
这条石板路要根据特殊的规则才能前进：对于小易当前所在的编号为K的 石板，小易单次只能往前跳K的一个约数(不含1和K)步，
即跳到K+X(X为K的一个非1和本身的约数)的位置。 小易当前处在编号为N的石板，他想跳到编号恰好为M的石板去，
小易想知道最少需要跳跃几次可以到达。
例如：
N = 4，M = 24：
4->6->8->12->18->24
于是小易最少需要跳跃5次，就可以从4号石板跳到24号石板 
输入描述:
输入为一行，有两个整数N，M，以空格隔开。 (4 ≤ N ≤ 100000) (N ≤ M ≤ 100000)


输出描述:
输出小易最少需要跳跃的步数,如果不能到达输出-1

输入例子1:
4 24

输出例子1:
5
'''

'''
解题思路：广度优先搜索算法（BFS）?  动态规划？
  使用BFS进行搜索，开始打算用递归，超时了，通过率只有50%，想着python递归效率低，就用循环重新实现了一遍，
  仍超时，通过率只有50%，不知道是不是还有巧妙的方法，有的话请赐教！
  查看了解析，看见大家都是用动态规划做的，我自己也用动态规划做了一遍，通过率只有40%，反而降低了...
  虽然通过率不高，但我觉得我写的几个方法都还可以...
'''

'''
方法一和方法二都只有50%的通过率
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为50.00%
方法三只有40%的通过率
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为40.00%
'''
# #方法一
# N, M = [int(each) for each in input().split()]
#
# searched = set()
# init_set = set()
# init_set.add(N)
#
#
# def jump(current_set):
#     wait_set = set()
#     for each in current_set:
#         if each == M:
#             return 0
#         else:
#             searched.add(each)
#             for k in range(2, each):
#                 if each % k == 0 and each+k not in searched:
#                     wait_set.add(each+k)
#     if min(wait_set) <= M:
#         temp = jump(wait_set)
#         if temp == -1:
#             return -1
#         else:
#             return 1 + temp
#     else:
#         return -1
#
# print(jump(init_set))
#
# # 方法二
# from collections import deque
# N, M = [int(each) for each in input().split()]
#
# d = deque()
# d.append(N)
# flag = False
# searched = set()
# count = 0
# while min(d) <= M:
#     length = len(d)
#     for i in range(length):
#         current = d.popleft()
#         if current == M:
#             flag = True
#             print(count)
#             break
#         else:
#             searched.add(current)
#             for k in range(2, current):
#                 if current % k == 0 and current+k not in searched:
#                     d.append(current+k)
#     if not flag:
#         count += 1
#     else:
#         break
# if not flag:
#     print(-1)


# 方法三
N, M = [int(each) for each in input().split()]

min_steps = [0]
for i in range(N+1, M+1):
    temp_list = []
    for j in range(N, i):
        if min_steps[j - N] != None:
            for k in range(2, j):
                if j % k == 0:
                    if j + k == i:
                        temp_list.append(min_steps[j-N] + 1)
        else:
            continue
    if temp_list:
        min_steps.append(min(temp_list))
    else:
        min_steps.append(None)

if min_steps[M-N] == None:
    print(-1)
else:
    print(min_steps[M-N])

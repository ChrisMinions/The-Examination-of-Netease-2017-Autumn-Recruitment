'''
[编程题] 回文序列
时间限制：1秒
空间限制：32768K
如果一个数字序列逆置之后跟原序列是一样的就称这样的数字序列为回文序列。例如：
{1, 2, 1}, {15, 78, 78, 15} , {112} 是回文序列, 
{1, 2, 2}, {15, 78, 87, 51} ,{112, 2, 11} 不是回文序列。
现在给出一个数字序列，允许使用一种转换操作：
选择任意两个相邻的数，然后从序列移除这两个数，并用这两个数字的和插入到这两个数之前的位置(只插入一个和)。
现在对于所给序列要求出最少需要多少次操作可以将其变成回文序列。

输入描述:
输入为两行，第一行为序列长度n ( 1 ≤ n ≤ 50) 第二行为序列中的n个整数item[i] (1 ≤ iteam[i] ≤ 1000)，以空格分隔。


输出描述:
输出一个数，表示最少需要的转换次数

输入例子1:
4 1 1 1 3

输出例子1:
2
'''

'''
解题思路：审题+递归
   审题：相邻两个数字之和放入数列的位置是这两个数字中前一个数字的位置，比如 1 2 3 4 5 6， 如果合并1和2，
   那么新数列是3 3 4 5 6
   思路：不断比较第一个数和最后一个数，若其不相等，则用转换操作调整第一个数和最后一个数，直至其相等
   递归：定义函数calc来计算所需要的操作数，calc函数以序列为输入参数。
   1、比较输入calc的序列的第一个和最后一个数，若相等，则把这两个数踢出序列后把新序列再次输入calc
   2、若第一个数大于最后一个数，则将第一个数和第二个数相加的和作为第一个数其余的数不变作为新的序列输入calc，此时计数+1
   3、若第一个数小于最后一个数，则将最后一个数和最后第二个数相加的和作最后一个数其余的数不变作为新的序列输入calc，此时计数+1
   4、序列的长度为0或1，则迭代结束
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
digs = [int(each) for each in input().split()]


def calc(dig_list):
    length = len(dig_list)
    if length == 1 or length == 0:
        return 0
    else:
        if dig_list[0] == dig_list[-1]:
            return calc(dig_list[1:-1])
        elif dig_list[0] > dig_list[-1]:
            temp = dig_list[-1] + dig_list[-2]
            temp_list = dig_list[:-2]
            temp_list.append(temp)
            return 1 + calc(temp_list)
        else:
            temp = dig_list[0] + dig_list[1]
            temp_list = dig_list[1:]
            temp_list[0] = temp
            return 1 + calc(temp_list)

print(calc(digs))

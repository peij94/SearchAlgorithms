"""
HJ16 购物单
动态规划问题
"""
# 先处理输入
import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    a = line.split()
    lst.append(a)

N = lst[0][0]
m = lst[0][1]

path = []  # 当前已选物件
curr_options = set(range(1, m)) - set(path)
curr_
for i in curr_options:
    if lst[i][2] == 0:
        path.append(i)



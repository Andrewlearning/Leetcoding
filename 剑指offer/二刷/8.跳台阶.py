"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = [0]*(n+1)
            res[0] = 0
            res[1] = 1
            res[2] = 2

            for i in range(3,n+1):
                res[i] = res[i-1] + res[i-2]

            return res[n]

"""
这样写就比上面那题节省空间多
"""
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
"""
class Solution(object):
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 假如 n > 1 and self.sumNums(n - 1) 为False
        # 那么self.sumNums(n - 1)就无法继续递归下去了，就往下面的self.res += n执行了。
        n > 1 and self.sumNums(n - 1)

        # 利用回溯来完成加减
        self.res += n
        return self.res


# 链接：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/

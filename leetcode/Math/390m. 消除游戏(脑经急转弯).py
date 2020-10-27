"""
给定一个从1 到 n 排序的整数列表。
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
返回长度为 n 的列表中，最后剩下的数字。

输入:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

"""


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        return 2 * (n / 2 + 1 - self.lastRemaining(n / 2))

# https://www.acwing.com/video/1779/
# 文字解析 https://www.acwing.com/solution/content/14240/


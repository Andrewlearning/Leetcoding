"""
给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。

如不存在这样的两个元素，请返回 -1。

示例 1：
输入：A = [34,23,1,24,75,33,54,8], K = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：A = [10,20,30], K = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。
"""

import sys
class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A and len(A) == 0:
            return []

        res = -sys.maxsize
        A.sort()

        l = 0
        r = len(A) - 1

        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            # 题目有明确说是小于 K 的两数之和
            elif A[l] + A[r] < K:
                res = max(res, A[l] + A[r])
                l += 1

        # 有可能不存在两数之和小于 K 这种情况
        return -1 if res == -sys.maxsize else res


"""
本题做法，排序后双指针
"""
"""
在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。

你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。



示例1:

输入: [1,4], 2
输出: 4
原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
第 4 秒初，提莫再次攻击艾希，使得艾希获得另外 2 秒中毒时间。
所以最终输出 4 秒。
"""


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            # 看中毒的时间短还是 下一次攻击的时间短
            total += min(timeSeries[i + 1] - timeSeries[i], duration)

        # 最后一次攻击，由于没有时间间隔了，那就默认它接下来再中一次毒
        return total + duration

# 链接：https://leetcode-cn.com/problems/teemo-attacking/solution/ti-mo-gong-ji-by-leetcode/

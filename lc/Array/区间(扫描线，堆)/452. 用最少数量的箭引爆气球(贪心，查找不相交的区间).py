"""
给定气球的直径，求我们能最多一次射爆的量

输入:
[[10,16], [2,8], [1,6], [7,12]]

[1--------6]
  [2-------------8]
              [7-------------12]
                        [10--------16]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
"""
class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        """
            首先先针对气球的尾部进行排序
            为什么是尾部，因为尾部标志着弓箭射击到的最远距离
            [[10,16], [2,8], [1,6], [7,12]]
            
            [1--------6]
              [2-------------8]
                          [7-------------12]
                                    [10--------16]
            
            尽管这四个集合看起来都是连在一起
            1.我们从[1,6]出发，寻找在1~6这个范围内相交的集合
            2.最后找到[1,6] 和 [7,12]不相交，然后就从[7,12]开始找下一个有相交的区间
        """
        points.sort(key=lambda x: x[1])
        
        # 表明了有几个没有相互连接关系 气球组
        res = 1
        curEnd = points[0][1]

        for l, r in points[1:]:

            # 说明两个区间之间不相交，想射爆这两个区间则需要新的弓箭
            if curEnd < l:
                res += 1

                # 发现有不相交的区间，更换到下一个不相交区间，然后继续寻找不相交区间
                # 因为相交的区间，都可以被一支箭射爆
                curEnd = r

        return res

"""
时间复杂度：O(NlogN)。因为对输入数据进行了排序。
空间复杂度：O(1)，仅仅使用了常数空间。

435和452是同一道题，都是通过查找有多少个不重叠的区间来解题

解题思路
把问题转换成：最多能选取几个区间不重叠的区域
因为有重叠的区间，肯定会被其他弓箭射爆，所以我们只用记录有几个不重叠的区间，就是需要多少支箭

解题过程
1. 先把所有区间按照尾端点进行排序
2. 然后从第一个区间的尾端点开始往后看，看有没有覆盖到其他区间，覆盖到其他区间则跳过
当碰到覆盖不到的区间，则记录，并移动到下一个区间继续看

https://www.acwing.com/video/1853/

"""
"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        list = []
        for interval in intervals:
            # 1 表示升起
            # -1 表示降落
            list.append((interval[0], 1))
            list.append((interval[1], -1))

        # 我们首先按照房间的开始时间来排序
        # 其次再由房间的升降顺序来排序（降的放前面），因为假如说一个房间同时结束和开始，那么不应该重新开一个房间
        list.sort(key=lambda x: (x[0], x[1]))

        res = 0
        count = 0

        for pair in list:
            # 在这里统计每个房间的升降
            count += pair[1]
            # 记录每个房间同时升起来的次数
            res = max(res, count)

        return res


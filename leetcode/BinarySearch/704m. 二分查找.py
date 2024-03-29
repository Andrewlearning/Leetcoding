"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
"""
# [ )模式的二分查找
class Solution(object):
    def search(self, nums, target):

        return self.findLeft(nums, target)

    # 直接套用34题的模板
    def findLeft(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l if nums[l] == target else -1
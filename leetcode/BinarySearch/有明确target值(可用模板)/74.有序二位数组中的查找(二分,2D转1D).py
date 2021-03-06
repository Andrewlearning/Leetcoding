"""
题目说明了下一行的所有值比上一行的所有值都要大
这题应该用二分查找来做
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix and len(matrix) == 0:
            return False

        lr = len(matrix)
        lc = len(matrix[0])
        left = 0
        right = lr * lc - 1

        while left <= right:

            mid = (left + right) // 2

            # 注意这里 //的是lc
            i = mid // lc
            j = mid % lc

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

"""
Time: O(logn) Space:O(1)
答案：
1.由于这题说了下面一行绝对比上面一行大，所以我们可以直接把这个矩阵看作是一个有序数组
2.所以我们可以直接使用二分查找，唯一的有点不同就是，我们需要把mid转换成矩阵的格式

这题我们用二分查找的方式是等于把一个矩阵数组给铺开，铺成一个一维数组，然后就可以用二分查找了
所以为什么这题有上一行的最后一个，比下一行的第一个小，是能让我们使用二分查找的原因。
因为假如不满足的话，那么我们就不能保证这个一维数组是递增的

3.mid = (left+right)//2
  num = array[mid//len(array[0])][mid%len(array[0])]
"""
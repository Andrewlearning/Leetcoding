"""
罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

示例1:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
这个例子就是，一直是从左到右递减，所以一路加过去就好了

输入:"IV"
输出: 4

"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        l = len(s)

        # 我们首先将 最后一个元素的值给赋予到res上
        res = mapping[s[l - 1]]

        for i in range(l - 2, -1, -1):
            # 每次我们都只比较i,和 i+1 的大小关系
            # 左边数字比右边大， VI = 6 II = 2
            if mapping[s[i]] >= mapping[s[i + 1]]:
                res += mapping[s[i]]
            # 左边数字比右边小, IV = 4
            else:
                res -= mapping[s[i]]

        return res

"""
Time: O(n), Space: O(1)
答案：
小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数
"""
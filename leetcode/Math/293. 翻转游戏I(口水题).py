"""
和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。

请你写出一个函数，来计算出第一次翻转后，字符串所有的可能状态。
示例：

输入: s = "++++"
输出:
[
  "--++",
  "+--+",
  "++--"
]
"""
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = []

        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                res.append(s[:i] + "--" + s[i + 2:])

        return res
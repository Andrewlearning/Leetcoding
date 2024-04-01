"""
Given an input string, reverse the string word by word.
（按照单词来进行反转，但是要注意忽略掉前面的空格）
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # python中string是不可修改的，所以需要转换成list
        s = list(s)
        n = len(s)
        
        # i,j 对应原字符串单词的开头和结尾
        # ni,nj 对应移位后字符串单词的开头和结尾
        ni = i = 0

        while i < n:
            # 跳过多余的空格，让i落到单词的第一个字幕上
            if s[i] == " ":
                i += 1
                continue
            
            # 开始探索，并且让[j]的字母放在[nj]的位置上
            j = i
            nj = ni
            while j < n and s[j] != " ":
                s[nj] = s[j]
                nj += 1
                j += 1
            
            # 反转[ni ~ nj - 1]
            self.reverse(s, ni, nj - 1)

            # 假如移动后的nj还没有越界，TODO
            if nj < n:
                s[nj] = ' '

            # TODO
            ni = nj + 1
            i = j

        # TODO
        return ''.join(reversed(s[:ni - 1]))

    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

"""
// Time: O(n), Space: O(n)
https://www.acwing.com/video/1525/
答案参考 https://www.acwing.com/activity/content/code/content/2188279/

例子 "apple care"
     elppa  erac(先把每个单词反转一遍)
     care apple（最后整体反转一遍）得到结果

"""











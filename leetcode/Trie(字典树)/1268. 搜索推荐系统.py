"""
给你一个产品数组products和一个字符串searchWord，products
 数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词searchWord 的每一个字母后
推荐products 数组中前缀与searchWord 相同的最多三个产品。
如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入searchWord每个字母后相应的推荐产品的列表。


输入：products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mogse"
输出：
[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
[],
[],
[]]

"""
# 本题的每个节点，不单单要存储到下一个节点的字典
# 还要储存一个word列表，所以要用一个class
class Trie:
    def __init__(self):
        self.child = {}
        # 以当前为已走过的字母为前缀，且字典序排前三的单词列表
        self.words = []


class Solution:
    def suggestedProducts(self, products, searchWord):
        root = Trie()

        # 初始化字典树
        for word in products:
            self.addWord(root, word)

        res = []
        cur = root

        # 假如说当前这个字母已经不在字典树了，那我们则直接把后面字母的匹配结果设为空
        notInTrie = False
        for char in searchWord:
            # 当前char不存在，那么后续的单词存在也没意义了,因为往下输入肯定也不会找到任何一个单词
            # 遍历到下一个字母，直接append([]), 因为前缀已经对不上了
            if notInTrie or char not in cur.child:
                res.append([])
                notInTrie = True
            # 当前char存在，则把结果记录
            else:
                cur = cur.child[char]
                res.append(cur.words)

        return res

    def addWord(self, root, word):
        cur = root
        for char in word:
            if char not in cur.child:
                cur.child[char] = Trie()

           # 进到下一层
            cur = cur.child[char]

            # 往新的一层添加word,因为我们可以通过char访问到这层
            cur.words.append(word)

            # 然后对这个这个list进行排序
            cur.words.sort()

            # 假如list长度大于3，那么我们就要pop（）掉不在前三的单词
            if len(cur.words) > 3:
                cur.words.pop()


s = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
s.suggestedProducts(products, searchWord)
class Solution(object):
    def exist(self, board, word):

        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], 'X'
            res = dfs(i + 1, j, k + 1) or \
                  dfs(i - 1, j, k + 1) or \
                  dfs(i, j + 1, k + 1) or \
                  dfs(i, j - 1, k + 1)

            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

"""
这个做法比较好，没有使用额外的空间，做法比较简洁
"""
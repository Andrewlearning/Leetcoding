# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        cur = head

        while cur:
            # 我们只要求cur, cur.next的值不相等就好
            # 所以能保留重复数字中的其中一个
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next

            # 当cur.next跟 cur的值不一样了，说明可以连起来了
            cur = cur.next

        return head

"""
这题我们用不断更新head.next, 知道head.next到达一个不等于先前数的位置
然后才把head指针移向head.next
"""
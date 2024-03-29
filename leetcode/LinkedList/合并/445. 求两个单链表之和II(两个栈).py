"""
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
这题是正序求的，不像第一题是倒叙，可以直接加，这里需要处理一下，把正序变成倒叙
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return l1

        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        temp = 0
        head = None
        while stack1 or stack2 or carry:
            temp += carry
            carry = 0

            if stack1:
                temp += stack1.pop()
            if stack2:
                temp += stack2.pop()

            if temp >= 10:
                carry = temp // 10
                temp %= 10

            # 这里的连接是反着来连接 cur_node2 -> cur_node1(head) -> None
            cur_node = ListNode(temp)
            cur_node.next = head
            head = cur_node
            temp = 0

        return head

"""
https://leetcode.com/problems/add-two-numbers-ii/discuss/129192/clear-python-solution-using-stack
"""
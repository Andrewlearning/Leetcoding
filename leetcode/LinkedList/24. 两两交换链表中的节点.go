/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {

    if head == nil || head.Next == nil {
        return head
    }


    cur := head
    next := head.Next

    cur.Next = swapPairs(next.Next)
    next.Next = cur

    return next

}


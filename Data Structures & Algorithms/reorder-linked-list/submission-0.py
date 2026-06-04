# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find mid
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev = None
        curr = slow

        # 4 -> 3 -> null

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        half1 = head
        half2 = prev

        # 1 -> 5 -> 2 -> 4 -> 3
        # 1 -> 4 -> 2

        while half1 and half2.next:
            half1Nxt = half1.next
            half2Nxt = half2.next

            half1.next = half2
            half2.next = half1Nxt

            half1 = half1Nxt
            half2 = half2Nxt


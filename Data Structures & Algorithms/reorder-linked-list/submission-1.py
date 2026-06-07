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
        # [1,2], [5,4,3]
        # [1,2], [4,3]

        # Find the middle:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the list from slow

        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        half = prev

        # [1,2], [5,4,3]
        start = head

        while start:
            startNext = start.next
            halfNext = half.next
            start.next = half
            half.next = startNext
            start = startNext
            half = halfNext

        return head

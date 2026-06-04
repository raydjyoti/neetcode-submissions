# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Set 2 pointers.
        # 1st pointer at start, 2nd at start + n

        dummy = ListNode(0)
        dummy.next = head
        pointA = dummy
        pointB = dummy
        ahead = n

        while pointB and ahead > 0:
            ahead -= 1
            pointB = pointB.next

        while pointB:
            pointB = pointB.next

            if not pointB:
                pointA.next = pointA.next.next
                break

            pointA = pointA.next

        return dummy.next
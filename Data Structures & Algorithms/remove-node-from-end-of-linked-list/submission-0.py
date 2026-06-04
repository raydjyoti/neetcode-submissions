# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head

        while curr:
            l += 1
            curr = curr.next

        target = l-n+1

        curr = head
        prev = None

        while curr:
            target -= 1

            if target == 0:
                if prev:
                    prev.next = curr.next
                else: head = head.next

                break

            prev = curr
            curr = curr.next

        return head
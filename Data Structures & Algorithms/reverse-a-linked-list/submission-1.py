# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        prevNode = None

        if not head: return head

        while head2 and head2.next:
            nextNode = head2.next
            head2.next = prevNode
            prevNode = head2
            head2 = nextNode

        head2.next = prevNode
        return head2

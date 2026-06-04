# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head: return head

        # O O O O O
        slow = head
        fast = head.next

        while fast and fast.next:

            if (fast == slow or fast.next == slow): return True

            slow = slow.next
            fast = fast.next
            fast = fast.next


        return False

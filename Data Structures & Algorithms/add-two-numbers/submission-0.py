# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # To sum nums, we go from right to left
        # Since nums are already reversed, just go from left to right
        curr1 = l1
        curr2 = l2
        totalNode = ListNode(0, None)
        output = totalNode
        carry = 0

        while curr1 or curr2:
            curr1Val = curr1.val if curr1 else 0
            curr2Val = curr2.val if curr2 else 0
            total = curr1Val + curr2Val + carry

            if total > 9: 
                carry = total//10
                total = total%10
            else: carry = 0

            totalNode.next = ListNode(total, None)
            totalNode = totalNode.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next

        if carry > 0: totalNode.next = ListNode(carry, None)
        
        return output.next
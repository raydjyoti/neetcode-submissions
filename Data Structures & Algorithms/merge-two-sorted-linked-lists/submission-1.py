# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        output = ListNode()
        outputHead = output

        while h1 and h2:
            minVal = min(h1.val, h2.val)
            newNode = ListNode(minVal)

            output.next = newNode
            output = output.next

            if h1.val == minVal: h1 = h1.next
            else: h2 = h2.next

        if h1: output.next = h1
        if h2: output.next = h2

        return outputHead.next
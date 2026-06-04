# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newList = ListNode()
        outputList = newList
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val <= head2.val:
                newList.next = head1
                head1 = head1.next

            else:
                newList.next = head2
                head2 = head2.next

            newList = newList.next

        
        if head1: newList.next = head1
        elif head2: newList.next = head2

        return outputList.next
        
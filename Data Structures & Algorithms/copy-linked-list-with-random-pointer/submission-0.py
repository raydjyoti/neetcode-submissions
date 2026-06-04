"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = dict()
        copy = Node(0, None, None)

        curr = head
        prev = None
        newHead = None

        while(curr):
            new = Node(curr.val, None, None)
            store[curr] = new

            if prev: prev.next = new
            else: newHead = new

            prev = new
            curr = curr.next


        curr = head
        currNew = newHead

        while curr:
            random = curr.random

            if random: newRandom = store[random]
            else: newRandom = None

            currNew.random = newRandom

            curr = curr.next
            currNew = currNew.next

        return newHead

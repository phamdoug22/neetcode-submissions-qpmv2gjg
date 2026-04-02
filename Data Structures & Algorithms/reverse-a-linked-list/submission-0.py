# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        # 1 
        # [0].next = None ( 0 -> none)
        # 0
        # 1

        # 2
        # [1].next = 0 ( 1 -> 0 -> none)
        # 1
        # 2


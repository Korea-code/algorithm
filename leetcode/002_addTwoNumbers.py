# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        total = l1.val + l2.val + c
        result = ListNode(total % 10)
        if total >= 10:
            c = 1
        else:
            c = 0
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, c)
        return result

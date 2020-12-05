# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        head = ListNode()
        if l1.val <= l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        temp = head.next
        while l1 or l2:
            if l2 and not l1:
                temp.next = l2
                l2 = l2.next
            elif l1 and not l2:
                temp.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                temp.next = l2
                l2 = l2.next
            elif l2.val > l1.val:
                temp.next = l1
                l1 = l1.next
            temp = temp.next
        return head.next

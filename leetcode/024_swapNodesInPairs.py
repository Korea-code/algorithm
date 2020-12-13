# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head
        while node.next:
            temp = node.val
            node.val = node.next.val
            node.next.val = temp
            if node.next.next:
                node = node.next.next
            else:
                break
        return head

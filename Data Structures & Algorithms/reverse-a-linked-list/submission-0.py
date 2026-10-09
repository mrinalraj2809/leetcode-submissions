# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        res = None
        while(point!=None):
            tmp = ListNode(point.val)
            tmp.next = res
            res = tmp
            point = point.next
        return res
            
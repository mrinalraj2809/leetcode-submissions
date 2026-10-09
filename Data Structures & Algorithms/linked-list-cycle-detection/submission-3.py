# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        slowPoint = head
        fastPoint = head.next
        while(slowPoint != fastPoint and slowPoint and fastPoint):
            if fastPoint.next:
                slowPoint = slowPoint.next
                fastPoint = fastPoint.next.next
            else:
                break
        if(slowPoint == fastPoint):
            return True
        return False

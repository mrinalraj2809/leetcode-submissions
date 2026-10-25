# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        delete_at = length - n
        if delete_at == 0:
            return head.next
        point = head
        while delete_at>1:
            point = point.next
            delete_at -= 1
        point.next = point.next.next  

        return head
        
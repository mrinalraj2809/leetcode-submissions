# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        point = l3
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            unit = total % 10
            carry = total // 10
            
            temp = ListNode(unit)
            point.next = temp
            point = point.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            unit = total % 10
            carry = total // 10
            
            temp = ListNode(unit)
            point.next = temp
            point = point.next

            l1 = l1.next
        while l2:
            total = l2.val + carry
            unit = total % 10
            carry = total // 10
            
            temp = ListNode(unit)
            point.next = temp
            point = point.next

            l2 = l2.next
        while carry:
            unit = carry % 10

            temp = ListNode(unit)
            point.next = temp
            point = point.next

            carry = carry // 10
        return l3.next


        
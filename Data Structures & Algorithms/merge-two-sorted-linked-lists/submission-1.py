# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res= None
        point = res

        while(list1 and list2):
            if list1.val <= list2.val:
                if not res:
                    res = list1
                    point = res
                else:
                    res.next= list1
                    res = res.next
                list1 = list1.next
            else:
                if not res:
                    res = list2
                    point = res
                else:
                    res.next= list2
                    res = res.next
                list2 = list2.next
        while(list1):
            # tmp = ListNode(list1.val)

            if not res:
                res = list1
                point = res
            else:
                res.next= list1
                res = res.next
            list1 = list1.next
        while(list2):
            if not res:
                res = list2
                point = res
            else:
                res.next= list2
                res = res.next
            list2 = list2.next
        return point

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Have two store and 1 res
        # 1. Forward list with even indices in ascending order
        # 2. Reverse list with odd indices in reverse order
        # Stop in mid 
        # trace intil this mid
        # combine them into result

        # Using linkedlist
        left = head
        right = None
        temp = head

        # Reverse the second copy
        length = 0
        while temp:
            tmp = ListNode(temp.val)
            tmp.next = right
            right = tmp
            length += 1
            temp = temp.next

        # Build reordered list
        result = head
        # result = None

        counter = 0
        print(length)
        # while counter < (length//2):
        #     # Save next pointers BEFORE changing anything
        #     left_next = left.next
        #     right_next = right.next
        #     if result == None:
        #         result = head
        #     else:
        #         result.next = left_next
        #         result = result.next
        #     result.next = right
        #     result = result.next

        #     # if left_next:
        #     #     result.next = left_next
        #     #     result = result.next

        #     left = left_next
        #     right = right_next
        #     counter += 1
        # result.next = None
        # head = result
        while left and right and counter < (length//2):
            # Save next pointers BEFORE changing anything
            left_next = left.next
            right_next = right.next

            result.next = right
            result = result.next

            if length %2 == 0 and counter == (length//2) - 1:
                result.next = None
                break
            if left_next:
                result.next = left_next
                result = result.next


            left = left_next
            right = right_next
            counter += 1
        result.next = None

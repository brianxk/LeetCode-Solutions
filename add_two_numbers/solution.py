# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_ = l1
        l2_ = l2

        carry = 0

        while l1_ and l2_:
            sum_ = l1_.val + l2_.val + carry

            if sum_ > 9:
                sum_ -= 10
                carry = 1
            else:
                carry = 0

            l1_.val = sum_

            l1_ = l1.next
            l2_ = l2.next


    

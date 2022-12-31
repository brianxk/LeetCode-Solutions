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

        # Traverse both lists until one is depleted
        # l1 will be the result list
        while True:
            sum_ = l1_.val + l2_.val + carry

            if sum_ > 9:
                sum_ -= 10
                carry = 1
            else:
                carry = 0

            l1_.val = sum_

            if not l1_.next or not l2_.next:
                break

            l1_ = l1_.next
            l2_ = l2_.next
    
        # If l1 was depleted first, append the rest of l2 to l1
        # If l2 was depleted first or if both were depleted, skip this step
        if l2_.next:
            l1_.next = l2_.next

        # If any digits remain, traverse and add until no carry remains
        # If both lists were depleted, skip this step
        while l1_.next and carry:
            l1_ = l1_.next
            sum_ = l1_.val + carry

            if sum_ > 9:
                sum_ -= 10
                carry = 1
            else:
                carry = 0

            l1_.val = sum_

        # If both lists were depleted and a carry remains, add it to the most significant position
        if carry:
            l1_.next = ListNode(carry)

        return l1

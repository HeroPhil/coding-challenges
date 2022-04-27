# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    isFirst = True

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carryOver=False) -> Optional[ListNode]:

        a = l1.val if l1 is not None else 0
        b = l2.val if l2 is not None else 0
        c = 1 if carryOver else 0

        sum = a + b + c

        co = sum >= 10

        sum = sum % 10

        result = ListNode(sum)

        # if end is reached
        if not self.isFirst and sum == 0 and l1 is None and l2 is None:
            self.isFirst = True
            return

        self.isFirst = False

        if l1 is not None or l2 is not None:
            result.next = self.addTwoNumbers(
                l1.next if l1 is not None else None, l2.next if l2 is not None else None, co)

        return result

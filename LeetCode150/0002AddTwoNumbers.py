# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        prev = res
        start = res
        carry = 0

        while l1 != None or l2 != None:
            if res != start:
                prev = prev.next

            if l1 == None:
                new = l2.val + carry
                if new > 9:
                    res.val = (l2.val + carry) % 10
                    carry = 1
                    l2 = l2.next
                    res.next = ListNode()
                    res = res.next
                else:
                    res.val = l2.val + carry
                    carry = 0
                    l2 = l2.next
                    res.next = ListNode()
                    res = res.next
                continue

            if l2 == None:
                new = l1.val + carry
                if new > 9:
                    res.val = (l1.val + carry) % 10
                    carry = 1
                    l1 = l1.next
                    res.next = ListNode()
                    res = res.next
                else:
                    res.val = l1.val + carry
                    carry = 0
                    l1 = l1.next
                    res.next = ListNode()
                    res = res.next
                continue

            new = l1.val + l2.val

            if new > 9:
                res.val = (new + carry) % 10
                carry = 1
                res.next = ListNode()
                res = res.next
                l1 = l1.next
                l2 = l2.next
            else:
                res.val = new + carry
                carry = 0
                res.next = ListNode()
                res = res.next
                l1 = l1.next
                l2 = l2.next

        if carry == 1:
            res.val = 1
            return start
        else:
            res = None
            prev.next = None
            return start
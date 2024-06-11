# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         id_list = []
#         curr = head
#         next = None
#         while curr != None:
#             next = curr.next
#             if next == head:
#                 return False
#             curr.next = head
#             curr = curr.next

#         return True


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        curr = head
        while curr != None:
            if curr.val != 100001:
                curr.val = 100001
                curr = curr.next
            else:
                return True

        return False
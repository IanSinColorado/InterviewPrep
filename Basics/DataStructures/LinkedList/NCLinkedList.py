# From NeetCode
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
   # LinkedList() will initialize an empty linked list. 
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    # int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr != None:
            if i == index:
                return curr.val
            
            i += 1
            curr = curr.next
        
        return -1


    # void insertHead(int val) will insert a node with val at the head of the list.
    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            # If the list was empty before inerting
            self.tail = newNode

    # void insertTail(int val) will insert a node with val at the tail of the list.
    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = self.tail.next
        # self.tail = self.tail.next
        
    # int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        # make curr the node just before our target node
        while i < index and curr != None:
            i += 1
            curr = curr.next

        # curr might be the final node or a middle node
        
        if curr and curr.next:
            # in case we are trying to remove tail
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True
        

        return False
        
    # int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
    def getValues(self) -> list[int]:
        curr = self.head.next

        rList = []
        while curr != None:
            rList.append(curr.val)
            curr = curr.next

        return rList
        

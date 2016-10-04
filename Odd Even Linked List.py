# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        odd = head
        even = evenHead = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        
        return head
#思路是一次處理兩個, 用odd.next = even.next把odd的接起來
#然後把even.next = odd.next把even的接起來
#最後把odd.next指到evenHead

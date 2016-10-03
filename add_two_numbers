# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        counter = 1
        head = ListNode(None)
        
        while l1 or l2 or carry:
            sum = carry
            
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            
            carry = sum / 10
            digit = sum % 10
            
            if counter == 1:
                head.val = digit
                node = head  #alias, called by reference
            else:
                node.next = ListNode(digit)
                node = node.next
            counter += 1
        return head
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        

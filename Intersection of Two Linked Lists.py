# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if pa is None:
                gc.collect()
                pa = headB
            else:
                pa = pa.next
            if pb is None:
                pb = headA
                gc.collect()
            else:
                pb = pb.next
            
        return pa
        

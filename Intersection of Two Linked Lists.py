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

"""
這題比較tricky一點, 就是pa不等於pb的時候（因為他們必定在某個地方會）
假設pa 的長度是 a' + c
pb的 b' + c
pa到底的時候接到pb, pb到底的時候接到pa

(a' + c + b') + c = (b' + c + a') + c
"""

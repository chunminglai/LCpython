# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
"""
實作linked list deleteNode的function, 
比如說1->3->5->7
然後給了5這個node
要把5.val = 5.next.val
然後5.next = 7.next這樣

"""

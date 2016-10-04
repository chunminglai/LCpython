# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #find mid node
        p = slow.next # head
        second_reverse = None
        while (p):
            next = p.next
            p.next = second_reverse
            second_reverse = p
            p = next
        s1 = head
        s2 = second_reverse
        

        while (s2):
            if s1.val != s2.val:
                return False
            s1 = s1.next
            s2 = s2.next
        return True    
### 上面是O(1) space but O(n) time的
### 如果不reverse來比的話可以參考下面這個寫法

def isPalindrome(self, head):

    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    
    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    
    return True

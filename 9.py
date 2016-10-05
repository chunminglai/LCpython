class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t = x
        if (x<0): 
            return False
        if (x==0):
            return True
        if (x%10==0):
            return False
        if (x<10):
            return True
        sum = 0
        while( x > sum):
            sum = (sum * 10) + (x % 10)
            x = x / 10
        #print sum
        if((sum==x) or (x==sum/10)):
            return True
        else:
            return False

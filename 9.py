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
"""
給定一個數字, 判斷其是不是回文, 比如說 121, 1221, 12321, 123321這種都是
先做邊界條件設定, 負數一定不是, 0～9是, 可以被十整除的也不是, 因為他最後位會是0
然後創造另一個數為sum, 每次把input x 的最末位弄出來 * 10, 等到兩個數字一樣的時候比較
如果一樣的話就是回文, 或者是 x == sum / 10這種情況 （odd digits situation ex. 121, 12321）

"""

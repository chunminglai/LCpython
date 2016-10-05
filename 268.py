class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in nums:
            n += i
        k = len(nums)
        #print n
        #print k
        N = (k * (k+1)) / 2
        return (N - n)
    
"""

數學題, 找出陣列裡面少了哪一個數
因為1~n的和是 n*(n+1) / 2
因為每個元素剛好出現一次, 所以就用Ｎ-n即可找到答案
"""

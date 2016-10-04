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

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=0
        print len(nums)
        for n in nums:
            if n != 0:
                nums[k] = n
                k += 1
        while(k<len(nums)):
            nums[k]=0
            k += 1

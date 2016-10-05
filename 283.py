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

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

思路, 邊走邊把不是零的element移到前面, 然後記錄遇到幾個零, 最後等到跑完的時候, 再把記錄零的個數的值慢慢append到後面去
就完成了

"""

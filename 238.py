class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = [0]*100  # output = list()
        for i in range(0,n,1):
            output[i] = 
            p *= nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] *=p
            p *=nums[i]
        return output

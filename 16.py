class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 1:
            return nums[0]+nums[1]
        nums = sorted(nums)
        ans = nums[0]+nums[1]+nums[2]
        
        for i,v in enumerate(nums[:-2]):
            j = i+1
            k = len(nums)-1
            while(j<k):
                sum = v + nums[j] + nums[k]
                if(abs(sum-target)<abs(ans-target)):
                    ans = sum
                if sum > target:
                    k = k-1
                else:
                    j = j+1
        return ans

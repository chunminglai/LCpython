class Solution(object):
    def twoSum(self, nums, target):
        
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]],i]
            else:
                buff_dict[target - nums[i]] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        target_num_dict = {}                                # stores the expected number (target-num) and it's index
        for idx, num in enumerate(nums):
            if (target-num) in target_num_dict:             # if the target already exists in the dictionary- we're done :) 
                return [ target_num_dict[target-num][1], idx]
            target_num_dict[num] = ( target-num , idx )     # else add the tuple to target_num_dict
        return None

"""

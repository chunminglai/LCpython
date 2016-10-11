class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >=1 and v==nums[i-1]:
                continue
            dic = {}
            for x in nums[i+1:]:
                if 0-v-x in dic:
                    res.add((v,x,-v-x))
                dic[x] = 1
        return list(list(item) for item in res)
        
"""
重點： 先sort, set的宣告, dictionary的宣告 跟2sum思路有點像

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = sorted(nums)
        
        if len(nums) < 2:
            return len(nums)
        i = 1
        ans = 1
        while(i < len(nums)):
            if(nums[i-1] != nums[i]):
                ans = ans+1
                nums[ans-1] = nums[i]
            i = i+1
        #print(type(ans))
        return ans

"""
要做的事除了return有幾個distinct value之外還要把nums的前Ｎ個的值改成distinct, 但是後面不管
大概就是簡單的list操作了

"""

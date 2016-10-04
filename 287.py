class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        
        while (low < high):
            count = 0
            mid = low + (high - low) / 2
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low
                    

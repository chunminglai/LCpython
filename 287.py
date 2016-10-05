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
                    
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

思路：二元搜尋法, low 一開始等於 1, high = n-1, 先跑一次, 如果low~mid的次數大於mid的話, 那代表要找的那個數一定在low與mid之間
不然就是再另一邊, 然後一直找到low = high為止, 那個數就是要找的target了
"""

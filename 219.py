Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

题目大意：
给定一个整数数组nums与一个整数k，当且仅当存在两个不同的下标i和j满足nums[i] = nums[j]并且| i - j | <= k时返回true，否则返回false。

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()
        for i, n in enumerate(nums):
        	if i > k:
        		dic.pop(nums[i-k-1],None)
        	if n in dic:
        		return True
        	else:
        		dic[n] = 1
        return False
"""       
先看一下例子[2,5,8,7,2]

用字典的資料結構, dic[key]有被set的話代表在k的範圍裡面
i, n enumerate的用法要記熟, 0, 第一個元素, 1, 第二個元素以此類推

pop的用法也要記熟
可以參考這個連結
https://docs.python.org/3/library/stdtypes.html#dict.pop
"""

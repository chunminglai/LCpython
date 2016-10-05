class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        se = set(nums)
        if (len(nums) > len(se)):
            return True
        else:
            return False
"""
把list轉成set的用法, se = set(nums)
複習宣告陣列的方法  nums = []
宣告字典的方法 buff_dict = dict() buff_dict = {}

接著比較set與list元素的個數即可
"""

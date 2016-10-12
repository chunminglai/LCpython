class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_until = 0
        if (strs==[]):
            return ""
        bench = strs[0]
        for i in range(0,len(bench)):
            for j in strs:
                if i >= len(j) or bench[i] != j[i]:
                    common_until = i
                    return bench[0:common_until]
        return bench
"""
問題是要找對所有的string找最長的prefix, 而不是substring
substring要用一個什麼ＫＭＰ的算法
反正就應幹吧, 找第一個先當成基準, 然後對每一個string 如果 i >=len(j) or bench[i] ! = j[i]
則回傳0到那個index之間的長度

"""

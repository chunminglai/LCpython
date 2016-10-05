class Solution(object):
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        i = 0
        j = len(height) - 1
        M = 0
        while ( i < j ):
            M = max(M,(j-i)*min(height[i], height[j]))
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return M
        """
        :type height: List[int]
        :rtype: int
        """

"""
/*
    设置两个指针i, j, 一头一尾, 相向而行. 假设i指向的挡板较低, j指向的挡板较高(height[i] < height[j]).
    下一步移动哪个指针?
    -- 若移动j, 无论height[j-1]是何种高度, 形成的面积都小于之前的面积.
    -- 若移动i, 若height[i+1] <= height[i], 面积一定缩小; 但若height[i+1] > height[i], 面积则有可能增大.
    综上, 应该移动指向较低挡板的那个指针.
*/
來源
https://discuss.leetcode.com/topic/35117/share-my-short-java-code-with-%E4%B8%AD%E6%96%87-explanation
"""

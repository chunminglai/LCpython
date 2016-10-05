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
        

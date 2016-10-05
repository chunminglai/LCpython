class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        #output = [0]*100  # 
        output = list()
        for i in range(0,n,1):
            output.append(p) 
            p *= nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] *=p
            p *=nums[i]
        return output
"""
思路:一個list中只有自己沒有被乘到, 所以可以用兩個index p, q
一個從頭開始乘, 一個從尾開始乘, 然後把兩邊*在一起, 掠過自己不乘就好
要注意的是在python中, 宣告list(array)添加元素基本上使用output.append(p)
如此在第十四行的地方就可以針對已訂位的元素操作
"""
    
   

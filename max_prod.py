class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans , maxp, minp = nums[0], 1, 1   
        for num in nums:            
            maxp, minp = max(num, minp * num, maxp * num), min(num, minp * num, maxp * num)
            ans = max(ans, maxp)
        return ans
        
        
      
     # followed sol : https://leetcode.com/problems/maximum-product-subarray/discuss/1337502/Python-3-O(n)-Solution-Hints-with-Spoiler

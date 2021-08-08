# Kadane's algo : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Works only for cases where -ve and +ve values are present. Eg.: [-2,1,-3,4,-1,2,1,-5,4] ; [1] ; [5,4,-1,7,8]
# Does not work when 1. length of array is 1 or has only -ve values

'''class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        array_sum = 0
        for i in nums:
            array_sum = array_sum + i
            if max_sum < array_sum:
                max_sum = array_sum
            if array_sum < 0:
                array_sum = 0
        return(max_sum)'''


#sol same as max_prod.py

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans , maxp, minp = nums[0], 0, 0   
        for num in nums:            
            maxp, minp = max(num, minp+num, maxp+num), min(num, minp+num, maxp+num)
            ans = max(ans, maxp)
        return ans
        
        

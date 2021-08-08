class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return (min(nums))  ---> time complexity O(n)
        
        #the below has O(log n) time complexity
        low , high = 0, len(nums)-1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] > nums[high]:
                low = mid +1
            else:
                high = mid
                
        return nums[high]

    #https://medium.com/@samip.sharma963/binary-search-and-its-big-o-3333d13bd6ec
    #https://hackernoon.com/binary-search-in-detail-914944a1434a

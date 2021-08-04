class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            #print(i)
            if i not in d:
                d[i] = nums.count(i)
        
        if max(d.values())>=2:
            return True
        else:
            return False
                
        #print(d)

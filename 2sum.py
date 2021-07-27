
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        output = []
        for i in nums:
            #print(i)
            a = nums.index(i)
            if abs(target-i) in nums[a+1:]:
                #print(nums[a+1:])
                #print(nums.index(i),nums.index(abs(target-i)))
                output.append(nums.index(i))
                output.append(nums.index(abs(target-i)))
                break

        return output
        

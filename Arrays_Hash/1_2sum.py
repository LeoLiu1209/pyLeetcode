class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result.get(diff), i]
            result[nums[i]] = i

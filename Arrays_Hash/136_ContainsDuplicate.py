class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #map
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = 1
        return False

        #set
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

        #set with Len
        return  len(set(nums)) != len(nums)
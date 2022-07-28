from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.
        """
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()
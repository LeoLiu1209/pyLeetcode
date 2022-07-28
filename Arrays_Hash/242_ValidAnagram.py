class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        # if no key in dict, use get can return a default assign value.
        """
        if len(s) != len(t):
            return False
        
        sMap, tMap = {}, {}
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        return sMap == tMap
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        result=0
        dict_set=set()
        for r in range(len(s)):
            while s[r] in dict_set:
                dict_set.remove(s[l])
                l+=1
            dict_set.add(s[r])
            result=max(result,r-l+1)
        return result

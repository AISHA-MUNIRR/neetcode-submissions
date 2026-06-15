class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1={}
        set2={}
        for i in range (len(s)):
            set1[s[i]]= set1.get(s[i],0)+1
        for j in range (len(t)):
            set2[t[j]]= set2.get(t[j],0)+1
        return set1 == set2
        
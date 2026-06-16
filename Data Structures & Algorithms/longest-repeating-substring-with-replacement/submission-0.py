class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result=0
        hash_set={}

        for r in range(len(s)):
            hash_set[s[r]]= 1+ hash_set.get(s[r],0)
            if (r-l+1 - max(hash_set.values())) > k :
                hash_set[s[l]]-=1
                l+=1
            result= max(result,r-l+1)
        return result

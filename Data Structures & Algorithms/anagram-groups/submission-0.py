class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(strs)):
            if strs[i]==0:
                continue
            for j in range (len(strs)):
                if strs[j]==0:
                    continue
                if sorted(strs[i])==sorted(strs[j]):
                    if strs[i] not in hashmap:
                        hashmap[strs[i]]=[strs[j]]
                    else:
                        hashmap[strs[i]].append(strs[j])
                        strs[j]=0

        for s in strs:
            if s!=0 and s not in hashmap:
                hashmap[s]=s
        return list(hashmap.values())
                    

        
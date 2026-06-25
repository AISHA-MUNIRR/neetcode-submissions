class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb=[]
        ans=[]
        unique=set()
        def getAllCombinations (nums, index, target, comb, ans):
            if index == len(nums) or target<0:
                return
            if target == 0:
                key = tuple(sorted(comb))
                if key not in unique:
                    unique.add(key)
                    ans.append(list(comb))
                return

            comb.append(nums[index])
            getAllCombinations(nums, index+1, target-nums[index], comb, ans)
            getAllCombinations(nums, index, target-nums[index], comb, ans)
            comb.pop()
            getAllCombinations(nums, index+1, target, comb, ans) 
        getAllCombinations(nums, 0, target, [], ans)
        return ans
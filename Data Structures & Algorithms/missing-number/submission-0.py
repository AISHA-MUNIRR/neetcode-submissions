class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum=0
        n=len(nums)
        for i in range(n):
            actual_sum+=nums[i]
        expected= n*(n+1)//2
        missing=expected-actual_sum
    
        if missing==0:
            return 0
        else:
            return missing
        
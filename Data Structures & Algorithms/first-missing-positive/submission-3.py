class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while(i<n):
            current=nums[i]
            if 1<=current<=n and nums[current-1]!=current:
                nums[i],nums[current-1]=nums[current-1],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1       
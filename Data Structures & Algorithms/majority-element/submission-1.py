class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency={}
        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]]+=1
            else:
                frequency[nums[i]]=1
        for value,count in frequency.items():
            if count>=len(nums)//2:
                return value
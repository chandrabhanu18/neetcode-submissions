class Solution:
    def findMin(self, nums: List[int]) -> int:
        # answer=0
        # value=0
        # for i in range(1,len(nums)):
        #     if nums[i]<nums[i-1]:
        #         # return nums[i]
        #         answer=-1
        #         value=nums[i]
        #         break
        # if answer!=-1:
        #     return nums[0]
        # else:
        #     return value   
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]                
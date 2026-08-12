class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=0,x
        while(low<=high):
            mid=low+(high-low)//2
            answer=mid*mid
            if answer==x:
                return mid
            elif answer>x:
                high=mid-1
            else:
                low=mid+1
        return high             
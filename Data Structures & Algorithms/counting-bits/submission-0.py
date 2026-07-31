class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for num in range(n+1):
            One_count=0
            for i in range(32):
                if (1<<i)&num:
                    One_count+=1
            result.append(One_count)
        return result            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        result=[]
        t=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        for value,count in t.items():
            if k==0:
                break
            result.append(value)
            k-=1
        return result
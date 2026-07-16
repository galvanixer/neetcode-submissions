class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = [[] for _ in range(len(nums)+1)] 
        freqcount = {}
        for n in nums:
            freqcount[n] = 1 + freqcount.get(n,0)

        for (ky,v) in freqcount.items():
            res[v].append(ky)

        out = []
        for i in range(len(nums),0,-1):
            for n in res[i]:
                out.append(n)
                if len(out) == k:
                    return out
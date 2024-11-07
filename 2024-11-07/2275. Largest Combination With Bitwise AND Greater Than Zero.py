from collections import defaultdict
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = defaultdict(lambda:0)
        def bits(x):
            i = 0
            while x:
                if x&1:count[i]+=1
                i+=1;x//=2
        for i in candidates:
            bits(i)
        print(count.values())
        return max(count.values())

        
# 1xxxxx
from heapq import *
from collections import defaultdict
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        heapify(max_heap)#value,class pos
        N = len(classes)
        for i in range(N):
            x,y = classes[i]
            heappush(max_heap,[-1*(y-x)/(y*(y+1)),i])
        new_add = defaultdict(lambda:0)
        while extraStudents:
            val,pos = heappop(max_heap)
            extraStudents-=1;new_add[pos]+=1
            x,y = classes[pos];x+=new_add[pos];y+=new_add[pos]
            heappush(max_heap,[-1*(y-x)/(y*(y+1)),pos])
        ans = 0
        for i in range(N):
            x,y = classes[i];x+=new_add[i];y+=new_add[i]
            ans+=(x/y)
        return ans/N
# want to maximimze y-x / y(y+1)
        
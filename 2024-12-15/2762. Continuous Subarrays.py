from heapq import *
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        # |a1 a2 a3 .. ai|aj   an
        # aj makes minimum till now too low or maximin too high
        # possbile arrays made = 123...i
        # lets start with a2 and still check from j th position
        left = 0
        right = 0
        min_heap = [] 
        heapify(min_heap)#number and index
        max_heap = []
        heapify(max_heap)# - number and index
        while right < N: 
            # print(left,right,min_heap,max_heap,len(min_heap))
            if len(min_heap) == 0:#simpley add
                heappush(min_heap,[nums[right],right])
                heappush(max_heap,[-nums[right],right])
            else:
                new_minimum = min(min_heap[0][0],nums[right])
                new_maximum = max(-max_heap[0][0],nums[right])
                if new_maximum-new_minimum<=2:
                    heappush(min_heap,[nums[right],right])
                    heappush(max_heap,[-nums[right],right])
                    right+=1
                    continue
                else:
                    ans+=(right - left)# drop left index
                    left +=1
            while min_heap and left>min_heap[0][1]:heappop(min_heap)
            while max_heap and left>max_heap[0][1]:heappop(max_heap)
            
        while left<N:
            # print('left',left,min_heap,max_heap)
            while min_heap and left>min_heap[0][1]:heappop(min_heap)
            while max_heap and left>max_heap[0][1]:heappop(max_heap)
            if (-1*max_heap[0][0])-min_heap[0][0]<=2:
                    ans += (right - left) 
                    left += 1

        return ans
        
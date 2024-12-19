class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        passed = [0]*(N)
        chunk = 0
        for i in range(N):
            passed[arr[i]] = 1
            flag = True
            for j in range(i+1):
                if passed[j] == 0:
                    flag = False
            if flag == True:
                chunk+=1
        return chunk
                
        
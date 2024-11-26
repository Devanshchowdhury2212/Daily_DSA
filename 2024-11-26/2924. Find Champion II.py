class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0]*n
        for a,b in edges:
            indegree[b]+=1
        ans = []
        for i in range(n):
            if indegree[i] == 0:ans.append(i)
        if len(ans) == 1:return ans[0]
        else:return -1
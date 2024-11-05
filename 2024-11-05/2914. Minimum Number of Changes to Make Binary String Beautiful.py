class Solution:
    def minChanges(self, s: str) -> int:
        S = len(s)
        ans = 0
        for i in range(0,S,2):
            if s[i] != s[i+1]:ans+=1
        return ans
        
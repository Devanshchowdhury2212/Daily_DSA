class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = [0]*26
        ans = []
        for i in s:
            counter[ord(i)-ord('a')]+=1
        
        j = 25
        while j>=0:
            # print(j,ans)
            while j>=0 and counter[j] == 0:j-=1
            if j<0:break
            elif counter[j]<=repeatLimit:
                while counter[j]:
                    ans.append(chr(j+ord('a')))
                    counter[j]-=1
            else:
                currlimit = repeatLimit
                while currlimit:
                    ans.append(chr(j+ord('a')))
                    counter[j]-=1
                    currlimit-=1
                check = j-1
                while check>=0 and counter[check] == 0:check-=1
                if check<0:
                    j = -1
                else:
                    ans.append(chr(check+ord('a')))
                    counter[check]-=1
        return ''.join(ans)
        
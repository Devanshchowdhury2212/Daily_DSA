class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:return '1'+word
        comp = []
        count = 0
        last = ''
        for i in word:
            # print(i,last,count)
            if last == i and count == 8:
                comp.append(str(9));comp.append(i)
                count = 0;last = ''  
            elif last == i:
                count+=1
            elif last!=i:
                if count:comp.append(str(count));comp.append(last)
                count = 1
                last = i
            else:
                pass
        if count!=0:
            comp.append(str(count));comp.append(last)
            
        return ''.join(comp)

        
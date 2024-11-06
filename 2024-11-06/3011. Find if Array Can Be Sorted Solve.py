class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def bits(x):
            c = 0
            while x:
                if x&1:c+=1
                x//=2
            return c
        bit_count = {}
        nums_bit = []
        for i in nums:
            bit_count[i] = bits(i)
        nums_sorted = []
        for index,i in enumerate(nums):
            nums_bit.append(bit_count[i])
        currentbits = bit_count[nums[0]]
        prevsegmax = 0
        currentsegmin = nums[0]
        currentsegmax = nums[0]
        i = 0
        while i<len(nums):
            # print(prevsegmax,currentbits,currentsegmin,bit_count[nums[i]])
            if currentbits == bit_count[nums[i]]:
                if nums[i]<prevsegmax:return False
                currentsegmin = min(currentsegmin,nums[i])
                currentsegmax = max(currentsegmax,nums[i])
            elif currentsegmax > nums[i]:return False
            else:
                prevsegmax= currentsegmax
                currentbits = bit_count[nums[i]]
                currentsegmin = min(nums[i],currentsegmin)
                currentsegmax = max(currentsegmax,nums[i])
            i+=1
        return True


# 1,1,1|4,4  
# 1,1,1|4,4        

# 2,1,1,1,1
# 1,2,1,1,1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        a=[]
        l=[i for i in range(n+1)]
        for i in l:
            if i not in nums:
                return i

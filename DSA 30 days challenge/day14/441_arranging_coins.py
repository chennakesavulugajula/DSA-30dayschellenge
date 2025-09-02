from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''a=[]
        setn=set(nums)
        for i in setn:
            if i in nums and nums.count(i)>1:
                a.append(i)
        return a;'''
        a=[]
        freq=Counter(nums)
        for i in freq:
            if freq[i]>1:
                a.append(i)
        return a

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            nums1=sorted(set(nums))
            n=len(nums1)
            longest=1
            count=1
            for i in range(1,n):
                if nums1[i]==nums1[i-1]+1:
                    count+=1
                    longest=max(longest, count)
                else:
                    count=1
        return longest

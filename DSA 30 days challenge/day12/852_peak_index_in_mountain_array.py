class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        m=max(arr)
        for i in range(len(arr)):
            return arr.index(m)
        

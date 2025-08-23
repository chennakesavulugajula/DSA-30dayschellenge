class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums3=nums1+nums2
        nums3.sort()
        result=[]
        for i in range(len(nums3)):
            if nums3[i]!=0:
                result.append(nums3[i])
        return result.sort()
        pos=0
        for i in nums1:
            if i!=0:
                nums1[pos]=i
                pos+=1
        nums1.sort()
        nums2.sort()
        result=nums1+nums2
        result.sort()
        return result"""
        nums1[:]=nums1[:m]+nums2[:n]
        nums1.sort()
        

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            target=nums[i]
            count=0
            for j in range(len(nums)):
                if nums[j]<target:
                    count+=1
            a.append(count)
        return a
        

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        trip=sorted([nums[i],nums[j],nums[k]])
                        if trip not in result:
                            result.append(trip)
        return result

        

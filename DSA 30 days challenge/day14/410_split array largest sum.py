class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mid):
            count, curr = 1, 0
            for n in nums:
                if curr + n > mid:
                    count += 1
                    curr = 0
                curr += n
            return count <= k
        left, right = max(nums), sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

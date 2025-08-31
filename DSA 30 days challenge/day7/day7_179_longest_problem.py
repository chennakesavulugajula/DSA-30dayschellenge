class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        re = []
        for i in nums:
            re.append(str(i))
        def sort_key(x):
            return x * 10
        re.sort(key=sort_key, reverse=True)
        result = ""
        for i in re:
            result += i
        if result[0] == "0":
            return "0"
        return result
        

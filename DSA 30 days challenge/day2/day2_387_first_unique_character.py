class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        a=Counter(s)
        for i,ch in enumerate(s):
            if a[ch]==1:
                return i
        return -1
print(a)

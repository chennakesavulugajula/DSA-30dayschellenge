class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        ra=a[::-1]
        return a==ra
        

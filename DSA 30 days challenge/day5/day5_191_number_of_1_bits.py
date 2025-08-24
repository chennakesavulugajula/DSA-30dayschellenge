class Solution:
    def hammingWeight(self, n: int) -> int:
        bi=bin(n)
        st=bi[2:]
        add=0
        for i in st:
            if i=='1':
                add+=1
        return add

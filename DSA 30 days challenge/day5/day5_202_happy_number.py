class Solution:
    def isHappy(self, n: int) -> bool:
        n1=str(n)
        s1=0
        for i in n1:
            s1+=int(i)**2
        n2=str(s1)
        s2=0
        for i in n2:
            s2+=int(i)**2
        n3=str(s2)
        s3=0
        for i in n3:
            s3+=int(i)**2
        n4=str(s3)
        s4=0
        for i in n4:
            s4+=int(i)**2
        n5=str(s4)
        s5=0
        for i in n5:
            s5+=int(i)**2
        n6=str(s5)
        s6=0
        for i in n6:
            s6+=int(i)**2
        n7=str(s6)
        s7=0
        for i in n7:
            s7+=int(i)**2

        if s7==1:
            return True
        else:
            return False        

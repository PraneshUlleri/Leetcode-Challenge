class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls=len(s)
        lt=len(t)
        i,j=0,0
        count=0
        while(i<ls and j<lt):
            if s[i]==t[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
            
        if count==ls:
            return True

        else:
            return False

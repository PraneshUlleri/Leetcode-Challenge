class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a=""
        for i in range (0, len(s)//2):
            a= s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=a

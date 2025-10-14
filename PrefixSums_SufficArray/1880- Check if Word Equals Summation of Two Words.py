class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha= "abcdefghijklmnopqrstuvwxyz"
        di={}
        for i in range (0,len(alpha)):
            di[alpha[i]]=str(i)
        val1=''
        val2=''
        val3=''
        for i in range(len(firstWord)):
            val1=val1+di[firstWord[i]]
        
        for i in range(len(secondWord)):
            val2=val2+di[secondWord[i]]
        for i in range(len(targetWord)):
            val3=val3+di[targetWord[i]]
        sum= int(val1)+ int(val2)
        if sum==int(val3):
            return True 
        return False


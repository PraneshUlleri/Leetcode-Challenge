# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mn=1
        mx=n
        
        while (mn<=mx):


            if guess((mn+mx)//2) ==0 :
                return (mn+mx)//2
            elif guess((mn+mx)//2) ==1:
                mn =(mn+mx)//2 +1
            else:
                mx = (mn+mx)//2 -1
            
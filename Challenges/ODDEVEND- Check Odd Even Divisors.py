t= int(input())

while(t):
    
    a,b = map (int, input().split())

    if a<=0:
        print ("No")
        
    elif a>0:
        if b % a == 0:
            print("Yes")
        else:
           print("No")
    t-=1
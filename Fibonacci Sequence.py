# Deadend set the largest no till fibonacci sequence should proceeed.
# [ex] 10=>no. inputed then output would be -> 0,1,1,2,3,5,8
DeadEnd = int(input("Tell the highest number till which Fibonacci seqeunce should proceed. Ex.100 :  "))

# In here i have made 3 var which represents fibonacci no.s
FiN1 = 0
FiN2 = 1
FiN3 = FiN1 + FiN2

# In here the code is about updating the var into new value every time fin3 is pinted on the console
print (FiN1)
print (FiN2)

i=0 # Part of failsafe
while (FiN3 < DeadEnd):
    print (FiN3)
    FiN1 = FiN2
    FiN2 = FiN3
    FiN3 = FiN2 + FiN1
    # down here is fail safe in which if the code goes wrong while loop will not run infinite times instead it will stop at some point in future.
    if (DeadEnd < i ):
        break
    else:
        i += 1


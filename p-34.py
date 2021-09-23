#zip function
roll=[101,102,103,104]
name=["anis","roni","asa","hadia"]
print(list(zip(roll,name)))
#recursion
def fact (n):
    if n==1 :
       return 1
    else:
        return n*fact(n-1)
print(fact(10))


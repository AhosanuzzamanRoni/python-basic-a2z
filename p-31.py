def substraction(x,y):
     result=x-y
     print("result=",result)
substraction(200,20)
def message():
    print("no parameter")
message()
#returning value from function :
def add (a,b) :
    sum=a+b
    return sum
result=add(20,30)
print("result=",result)
#defined large function :
def large(a,b) :
    if a>b :
        return a
    else:
        return b

maximum=large
print(maximum(100,500))
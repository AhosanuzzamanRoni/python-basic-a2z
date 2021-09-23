#lambda functions
'''
1.a function without name anonymous function
2.not powerful as normal function
3.it can work with signle expression / singleline of code
'''
#ex-01
print((lambda a,b : a*a + 2*a*b + b*b)(2,3))
#ex-02
a=(lambda x : x*x*x)(3)
print(a)
#map & filter function
def square (x):
    return x*x
num=[1,2,3,4,5,6]
result=list(map(square,num))
print(result)
#filter function
num=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,num))
print(result)
#list comprehension format [ expression for item in list ]
num =[1,2,3,4,5]
result=[x*x for x in num]
result=[ x for x in num if x%2==0]
print(result)

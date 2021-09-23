'''num=[10,20,30,40,50]
print(num)
index=0
while index < 5 :
    print(num[index])
    index=index+1

num=[10,20,30,40,50]
print(num)
for x in num :
    print(x)

num=[10,20,30,40,50]
sum=0
for x in num :
    sum=sum+x
    print(sum)'''
#series:1+2+3+......+n=?
n=int(input("Enter the last number :"))
sum=0
for x in range (1,n+1,1):
    sum=sum+x
    print(sum)
# 2+4+6+....+N=?
n=int(input("Enter the last number :"))
sum=0
for x in range (2,n+1,2):
    sum=sum+x
    print(sum)
#1^2+2^2+3^3+.....+n^2=?
n=int(input("Enter the last number :"))
sum=0
for x in range (1,n+1,1):
    sum=sum+x*x
    print(sum)
#1*2*3*.....*n=?
n=int(input("Enter the last number :"))
sum=1
for x in range (1,n+1,1):
    sum=sum*x
    print(sum)

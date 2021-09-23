# xargs & xxargs args=argument,
# * this sign of strick symble
#xargs work at tuples


#using for loop
def add (*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
        print(sum)
add(10,20)
add(10,20,40,100)
#xxargs example
def student(**details):
    print(details)
student (id=101,name="roni")
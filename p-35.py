'''file=open("student.txt","r+")
 #checker


text=file.readlines()[0]
print(text)

file.close()
#using for loop :
file=open("student.txt","r+")
for line in file :
    print(line)
file.close()'''

#writing in a file
file=open("student1.txt","w")
file.write("\n sadi-lecturer of physics")
file.close()
#html file
file=open("HELLO.html","w")
file.write("<h1> this is a text </h1>")
file.close()
#swapping end of basic python
a=20
b=10
a,b=b,a
print("a=",a)
print("b=",b)
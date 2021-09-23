'''subjects=["c","c++","java","python","basic"]
subjects.append("toc")
subjects.insert(2,"05")
subjects.remove("basic")
subjects.sort()
subjects.reverse()
print(subjects)

subjects=[20,10,4,555]
#subjects.reverse()
subjects.pop()
print(subjects)
subjects=[20,10,4,555]
subjects2=subjects.copy()
print(subjects2)'''

subjects=[20,10,4,4,4.5,4,444,44,4,4,555]
#pos=subjects.index(4)
pos=subjects.count(4)
print(pos)

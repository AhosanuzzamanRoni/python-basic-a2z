#stack and queue
#stack -push & pop (push mean input,, pop mean remove by lifo)
books=[]
books.append("learn c")
books.append("learn c++")
books.append("learn java")
books.pop()
books.pop()
print(books)
# queue ( fifo system)
from collections import deque
bank = deque(["anis","karim","roni","asa","hadia"])

bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
if not bank :
    print("no person left")
print(bank)
class phone :
    def call (self):
        print("your self")

    def message(self):
        print("you can message")
class samsung(phone) :

    def photo(self):
        print(" you can take photo")

s=samsung()
s.call ()
s.photo ()
s.message ()
print(issubclass(samsung,phone))
#subclass/child clASS -- samsung
#superclass/prants class --phone

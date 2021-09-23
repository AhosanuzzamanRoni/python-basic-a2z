class phone :
    def _init_(self):
      print("i am in phone class")
class samsung(phone):
   def _init_(self):
    super()._init_()
    print("i am in samsung class")

s=samsung

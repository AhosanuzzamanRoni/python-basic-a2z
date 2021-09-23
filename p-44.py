'''import re
pattern=r"Colour"
text="my favourite Colour is red"
match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
else:
    print("not matched")

import re
pattern=r"colour"
text1="my favourit colour is red.i love blue colour"
text2=re.sub(pattern,"color",text1,count=1)
print(text2)'''
import re
pattern=r"[0-9]"
if re.match(pattern,"89dbunfd"):
    print("matched")
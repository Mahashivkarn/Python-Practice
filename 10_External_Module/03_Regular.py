import re

text="The Quick brown fox jumps over brown the  brown lazy dog."

match =re.search("brown",text)
print(match)
# if match:
#     print("Match Found!")
#     print("Start index:",match.start())
#     print("End index:",match.end())
    
match=re.findall("brown",text,re.IGNORECASE)#for case senstivness ignore.
print("Matches:",match)
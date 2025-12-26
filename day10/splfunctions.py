import re

mylist = []

# check if 2 is in the list
if 2 in mylist:
    print("2 is present in the list")
else:
    print("2 is not present in the list")

# regular expression search
s = "he ll o"
i = "e"

res = re.search(i, s)   # search pattern

if res:
    print("true")
else:
    print("false")

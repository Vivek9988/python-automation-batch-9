# slicing = substring
myString = "abcdef ghijkl"

# Slicing examples
sub1 = myString[0:6]     # first 6 characters → abcdef
sub2 = myString[7:]      # from index 7 till end → ghijkl
sub3 = myString[:5]      # first 5 characters → abcde
sub4 = myString[10]      # character at index 10 → k
sub5 = myString[-5:]     # last 5 characters → hijkl

print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)

# Membership check
if "a" in myString:
    print("a is there")

# Split string into words
word = myString.split(" ")
print(word)

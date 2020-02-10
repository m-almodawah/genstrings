from genstrings import GenStrings

mystr = GenStrings(3, "abc")

ss = mystr.nextstr()
while ss:
    print(ss)
    ss = mystr.nextstr()

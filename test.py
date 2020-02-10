from genstrings import GenStrings

mystr = GenStrings(3, "$3Ay")

ss = mystr.nextstr()
while ss:
    print(ss)
    ss = mystr.nextstr()

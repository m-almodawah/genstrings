An easy-to-use and a thread-safe python class for generating all possible strings of a given length from a given set of characters.

Example:
```
from genstrings import GenStrings

mystr = GenStrings(3, "abc")

ss = mystr.nextstr()
while ss:
    print(ss)
    ss = mystr.nextstr()
```

Output:
```
aaa
aab
aac
aba
abb
abc
aca
acb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc
```

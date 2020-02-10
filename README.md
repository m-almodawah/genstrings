An easy-to-use and a thread-safe python class for generating all possible strings of a given length from a given set of characters.

Example:
```
from genstrings import GenStrings

mystr = GenStrings(3, "$3Ay")

ss = mystr.nextstr()
while ss:
    print(ss)
    ss = mystr.nextstr()
```

Output:
```
$$$
$$3
$$A
$$y
$3$
$33
$3A
$3y
$A$
$A3
$AA
$Ay
$y$
$y3
$yA
$yy
3$$
3$3
3$A
3$y
33$
333
33A
33y
3A$
3A3
3AA
3Ay
3y$
3y3
3yA
3yy
A$$
A$3
A$A
A$y
A3$
A33
A3A
A3y
AA$
AA3
AAA
AAy
Ay$
Ay3
AyA
Ayy
y$$
y$3
y$A
y$y
y3$
y33
y3A
y3y
yA$
yA3
yAA
yAy
yy$
yy3
yyA
yyy
```

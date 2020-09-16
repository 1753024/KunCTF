## Digit

open the picture we have some numbers like:

11 21 14 3 20 6 { 10 21 19 20 12 5 20 20 5 18 14 21 13 2 5 18 19 }

use this code to decode a1z26

```
import string

letter = string.ascii_lowercase

cipher = "11 21 14 3 20 6 { 10 21 19 20 12 5 20 20 5 18 14 21 13 2 5 18 19 }"
text=""
for i in cipher.split(' '):
    if(i=="{" or i=="}"):
        text+=i
    else:
        text+=letter[int(i)-1]

print(text)
```

KunCTF{justletternumbers}
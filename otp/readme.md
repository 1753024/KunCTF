## OTP

Look at the table we notice that to find the text we need to find the character of the cipher in the key character column

use this code to decode

```
import string

cipher = 'OPOWVWROGGIOMJ'
key = 'THISISAKEY'

def ConvertToList(text):
    listchar=[]
    for char in text.lower():
        listchar.append(ord(char)-96)
    
    return listchar

def BalanceTheLenght(cipher,key):
    if(len(cipher)>len(key)):
        while(len(cipher)>len(key)):
            for char in key:
                if(len(cipher)<=len(key)):break
                key+=char
    else:
        while(len(cipher)<len(key)):
            for char in cipher:
                if(len(cipher)>=len(key)):break
                cipher+=char

    return cipher,key

def ConvertToString(numberList):
    text=""

    for num in numberList:
        text+=letter[int(num)-1]
    return text.upper()

cipher,key=BalanceTheLenght(cipher,key)
cipherList = ConvertToList(cipher)
keyList= ConvertToList(key)
answer=[]
letter = string.ascii_lowercase

for i in range(len(cipherList)):
    numChar=cipherList[i]-keyList[i]+1
    while(numChar>26):
        numChar-=26
    answer.append(numChar)


print(ConvertToString(answer))

```

KunCTF{VIGENERECIPHER}
#set1_3
import string
s='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print(int('0x1b',16))

for j in string.ascii_letters:
    #print(j)
    t=''
    for i in range(0,len(s),2):
        temp=int('0x'+s[i:i+2],16)
        #print(t)
        t=t+str(chr(temp^ord(j)))
    print(f'{j}:{t}')



#set1_2
def Fixed_XOR(a):
    b='686974207468652062756c6c277320657965'
    assert len(b)==len(a)
    a=int(a,16)
    ans=0
    ans=a^int(b,16)
    return ans

#a=input()
a='1c0111001f010100061a024b53535009181c'
print(hex(Fixed_XOR(a)))

#set1_8
from Crypto.Cipher import AES
import base64

def Detect_AES_in_ECB(ciphertext) :
    block_size = 16
    block = [ciphertext[i:i+block_size] for i in range(0,len(ciphertext),block_size)]
    Repeat = len(block) - len(set(block))
    _data = {
         'ciphertext': ciphertext,
         'Repeat': Repeat
    }
    return _data
        

def AES_in_ECB(ciphertext,key) :
    keyword = AES.new(key,AES.MODE_ECB)
    cipher = keyword.decrypt(ciphertext)
    return cipher

if __name__ == '__main__' :
    ciphertext = []
    for i in open('cryptopals_set1_8.txt') :
        _ciphertext = i.strip()
        ciphertext.append(_ciphertext)
    data = []
    for j in ciphertext:
        _data = Detect_AES_in_ECB(j)
        data.append(_data)
    result = sorted(data, key = lambda Repeat:Repeat['Repeat'],reverse=True)[0]
    print(result)

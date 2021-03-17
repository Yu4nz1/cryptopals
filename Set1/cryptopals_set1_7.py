#set1_7
from Crypto.Cipher import AES
import base64

def AES_in_ECB(ciphertext,key) :
    keyword = AES.new(key,AES.MODE_ECB)
    cipher = keyword.decrypt(ciphertext)
    return cipher

if __name__ == '__main__' :
    
    key = b'YELLOW SUBMARINE'
    with open('cryptopals_set1_7.txt') as of :
        ciphertext = base64.b64decode(of.read())
        print(ciphertext)
    cipher = AES_in_ECB(ciphertext,key) 
    print(cipher)


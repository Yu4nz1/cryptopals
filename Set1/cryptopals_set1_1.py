#set1_1
import base64 
str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str=bytes.fromhex(str)
print(base64.b64encode(str))


"""
手撸base64
不使用base64模块
"""
#set1_1
b64_dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b64_encode(s) :
    print(s)
    byte = ''.join([bin(i)[2:].zfill(8) for i in s])
    group = [byte[j:j+6] for j in range(0,len(byte),6) ] 
    print(group)
    b64_string=''
    for k in group : 
        print(k)
        if len(k)==6 :
            b64_string = b64_string + b64_dictionary[int(k,2)]
        elif len(k)==4 :
            b64_string = b64_string + b64_dictionary[int(k+'00',2)] + '='
        elif len(k)==2 :
            b64_string = b64_string + b64_dictionary[int(k+'0000',2)] + '=='
    return b64_string

def main():
    str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    byte_string = bytes.fromhex(str)
    print(b64_encode(byte_string))


if __name__ == '__main__':
    main()

"""
第一版
"""
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

"""
第二版
"""
    
#set1_3
import string
import re

def English_Scoring(t):
    latter_frequency = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': 1.3000
}
    return sum([latter_frequency.get(i,0) for i in t.lower()])     

s='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print(int('0x1b',16))

for j in string.ascii_letters:
# j:XOR'd Single_character
    #print(j)
    t=''
    # t: the XOR'd result
    score=0
    # score: scoring 't'
    for i in range(0,len(s),2):
        temp=int('0x'+s[i:i+2],16)
        #print(t)
        t=t+str(chr(temp^ord(j)))
        t=re.sub(r'[\x00-\x1F]+','', t) 
    score=English_Scoring(t)
    print(f'{j}:{t},{score}')

"""
第三版
"""
#set1_3
import string
import re
from operator import itemgetter, attrgetter
latter_frequency = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .15000
}

s='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def English_Scoring(t):
    return sum([latter_frequency.get(i,0) for i in t.lower()])     

def Single_XOR(j):
    t=''
    # t: the XOR'd result
    for i in range(0,len(s),2) :
        temp = int('0x'+s[i:i+2],16)
        t = t+str(chr(temp^ord(j)))
        t = re.sub(r'[\x00-\x1F]+','', t) 
        #remove the ascii control characters
    return t


_data=[]
for j in string.ascii_letters :
# j: XOR'd Single_character
# t: the XOR'd result
# score: Scoring 't'
    t = Single_XOR(j)
    score = English_Scoring(t)
    data = {
        'Single character' : j ,
        'result' : t,
        'score' : score
        }
    _data.append(data)
#print(_data)
best_score = sorted(_data, key = lambda score:score['score'], reverse=True)[0]
print(best_score)
"""
for i in best_score :
    print("{}: {}".format(i.title(), best_score[i]))

"""

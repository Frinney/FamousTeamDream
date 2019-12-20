import random

s = "`1234567890-=\]'/[;.(){}pl,okmijnuhbygvtfcrdxeszwaqPLMOKNIJBUHVYGCTFXRDZESWAQ/*\+!@#$%^&*"
psw = ''

for x in range(int(input())):
    psw += random.choice(s)

print(psw)
try:
    f = open('passwords.txt', 'a')
except IOError as e:
    f = open('passwords.txt', 'w')
finally:
    f.writelines(psw)
    f.write('\t')
    f.writelines('dfdhgfh')
    f.write('\n')
f.close()

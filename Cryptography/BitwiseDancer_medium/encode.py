m='REDACTED'
key='QUACK'
cipher=[]

index=0

for i in m:
    cipher.append((ord(key[index])^ord(i)))
    index=(index+1)%len(key)

print(cipher)

plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
code = ''
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    
         
    code += chr(cipherValue)
print(code)

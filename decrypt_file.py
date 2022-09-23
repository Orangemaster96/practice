fname=input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
with open(fname,"r") as file:
    code=file.read()
plainText = ''

for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    plainText +=  chr(cipherValue)
with open(output_file_name,"w") as new_file:
    new_file.write(plainText)
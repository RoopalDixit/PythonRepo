str=input()
output=''
print(str)
for char in str:
    b=''
    if char.isupper():
        b=char.lower()
        output=output+b
    else:
        b=char.upper()
        output=output+b
print(output)


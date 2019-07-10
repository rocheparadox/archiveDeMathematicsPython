field_length = int(input("Enter the length of the field: "))
a = input("Enter first binary value: ")
b = input("Enter second binary value: ")

a = int((a[:field_length]),2)
b = int((b[:field_length]),2)


print(a ^ b, bin(a^b))
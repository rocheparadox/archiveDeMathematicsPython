import sys

if len(sys.argv) > 1 :
    binary_number = sys.argv[1]
else:
    binary_number = input("Please enter a binary number to be converted into hex: ")
try:
    int(binary_number)
except BaseException:
    print("Input should be a binary value..")
    exit()

hex_value = hex(int(str(binary_number),2))
print(hex_value)


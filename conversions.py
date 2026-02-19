#Bailey Evan Reese
#PantherID: 002675242
#2/19/2026
#Computer Architecture - Task 1 - Data Systems


#decimal to binary logic
def decimalToBinary(decimal):
    #if the given decimal number is 0, return "0"
    if decimal == 0:
        return "0"
    binary = ""
    
    if decimal < 0:
        #if the given decimal number is negative, convert it to its two's complement representation by adding 2^32 to it
        decimal += 1 << 32

    #keep dividing the decimal number by 2 and appending the remainder to the binary string until the decimal number becomes 0
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

#binary to decimal logic
def binaryToDecimal(binary):
    decimal = 0
    #reverse the binary string and iterate through each character, multiplying it by 2 raised to the power of its index and adding it to the decimal number
    for index, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** index)
    return decimal

#binary to hexadecimal logic
def binaryToHexadecimal(binary):
    hexadecimal = ""
    #add padding to the binary string with leading zeros to make its length a multiple of 4
    while len(binary) % 4 != 0:
        binary = "0" + binary
    #iterate through the binary string in chunks of 4, converting each chunk to its corresponding hexadecimal digit and appending it to the hexadecimal string
    for i in range(0, len(binary), 4):
        chunk = binary[i:i+4]
        hexadecimal += hex(int(chunk, 2))[2:].upper()
    return hexadecimal
    
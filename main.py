#Bailey Evan Reese
#PantherID: 002675242
#2/19/2026
#Computer Architecture - Task 1 - Data Systems

from signedInputParser import signed32DecimalInputParser
from conversions import decimalToBinary, binaryToHexadecimal, binaryToDecimal

def main():
    #main loop that continues until the user decides to quit by entering 'Q'
    while True:
        userInput = input("Enter a signed decimal number and the wanted conversion type (or 'Q' to quit):")
        if userInput.upper() == "Q":
            break

        #get users desired conversion type and validate it, allowing the user to re-enter if it's invalid or quit if they choose to
        conversionType = input("Enter conversion type (DEC/BIN/HEX) or Q to quit: ").upper()
        if conversionType == "Q":
            break
        while conversionType not in ["DEC", "BIN", "HEX"]:
            conversionType = input("Invalid conversion type, Enter (DEC/BIN/HEX) or q to quit: ").upper()
            if conversionType == "Q":
                return
        try:
            signedDecimal = int(userInput)

            signedDecimal, saturationFlag, overflowFlag = signed32DecimalInputParser(signedDecimal)

            if conversionType == "DEC":
                print(f"Input: {signedDecimal}")
                if saturationFlag and overflowFlag:
                    print("saturationFlag 1")
                    print("overflowFlag 1")
                elif saturationFlag == False and overflowFlag == False:
                    print("saturationFlag 0")
                    print("overflowFlag 0")
                continue
            elif conversionType == "BIN":
                binary = decimalToBinary(signedDecimal)
                print(f"Binary: {binary}")
                if saturationFlag and overflowFlag:
                    print("saturationFlag 1")
                    print("overflowFlag 1")
                elif saturationFlag == False and overflowFlag == False:
                    print("saturationFlag 0")
                    print("overflowFlag 0")
            elif conversionType == "HEX":
                binary = decimalToBinary(signedDecimal)
                hexadecimal = binaryToHexadecimal(binary)
                print(f"Hexadecimal: {hexadecimal}")
                if saturationFlag and overflowFlag:
                    print("saturationFlag 1")
                    print("overflowFlag 1")
                elif saturationFlag == False and overflowFlag == False:
                    print("saturationFlag 0")
                    print("overflowFlag 0")

        except ValueError:
            print("Invalid input. Please enter a valid signed decimal number.")

if __name__ == "__main__":
    main()

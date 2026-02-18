from signedInputParser import signed32DecimalInputParser
from conversions import decimalToBinary, binaryToHexadecimal, binaryToDecimal

def main():
    while True:
        userInput = input("Enter a signed decimal number and the wanted conversion type (or 'Q' to quit):")
        if userInput.upper() == "Q":
            break

        conversionType = input("Enter conversion type (DEC/BIN/HEX) or Q to quit: ").upper()
        if conversionType == "Q":
            break
        while conversionType not in ["DEC", "BIN", "HEX"]:
            conversionType = input("Invalid conversion type, Enter (DEC/BIN/HEX) or q to quit: ").upper()
            if conversionType == "Q":
                return
        try:
            signedDecimal = int(userInput)
            #print(f"Original Input: {signedDecimal}")

            signedDecimal = signed32DecimalInputParser(signedDecimal)
            #print(f"Parsed Input: {signedDecimal}")

            if conversionType == "DEC":
                print(f"Input: {signedDecimal}")
                continue
            elif conversionType == "BIN":
                binary = decimalToBinary(signedDecimal)
                print(f"Binary: {binary}")
            elif conversionType == "HEX":
                binary = decimalToBinary(signedDecimal)
                hexadecimal = binaryToHexadecimal(binary)
                print(f"Hexadecimal: {hexadecimal}")

        except ValueError:
            print("Invalid input. Please enter a valid signed decimal number.")

if __name__ == "__main__":
    main()

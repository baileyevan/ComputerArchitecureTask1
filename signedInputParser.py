# This function takes a signed decimal number as input and checks if it is within the range of signed 32-bit integers. 
#If the input is less than the minimum value, it returns the minimum value. If the input is greater than the maximum value, 
#it returns the maximum value. Otherwise, it returns the input as is.
def signed32DecimalInputParser(signedDecimal):
    MIN32_INT = -(1 << 31)  # -2147483648
    MAX32_INT = (1 << 31) - 1  # 2147483647
    #check if the input is a valid integer and within the range of signed 32-bit
    if signedDecimal < MIN32_INT:
        return MIN32_INT
    elif signedDecimal > MAX32_INT:
        return MAX32_INT
    return signedDecimal
#Bailey Evan Reese
#PantherID: 002675242
#2/19/2026
#Computer Architecture - Task 1 - Data Systems


# This function takes a signed decimal number as input and checks if it is within the range of signed 32-bit integers. 
#If the input is less than the minimum value, it returns the minimum value. If the input is greater than the maximum value, 
#it returns the maximum value. Otherwise, it returns the input as is.
def signed32DecimalInputParser(signedDecimal):
    # -2147483648
    MIN32_INT = -(1 << 31)  
    # 2147483647
    MAX32_INT = (1 << 31) - 1  
    #check if the input is a valid integer and within the range of signed 32-bit
    saturationFlag, overflowFlag = False, False
    if signedDecimal < MIN32_INT:
        saturationFlag, overflowFlag = True, True
        return MIN32_INT, saturationFlag, overflowFlag
    elif signedDecimal > MAX32_INT:
        saturationFlag, overflowFlag = True, True
        return MAX32_INT, saturationFlag, overflowFlag
    return signedDecimal, saturationFlag, overflowFlag
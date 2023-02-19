'''
Determine whether each code is valid or not
Output results of codes to lists that will be called in Assign2.py
'''
#function removes last digit, sums each digit in the code number, modulo 10 the sum,
#and check if the last digit equals the sum modulo of 10
def BasicCode (userInput):
    newStr = userInput[:-1]
    lastDigit = int(userInput[-1])
    total = 0
    for i in range(len(newStr)):
        total = total + int(userInput[i])
    remain = total % 10
    if lastDigit == remain:
        base = True
    else:
        base = False
    return base
#function removes last digit, multiplies each digit by its corresponding position, modulo 10 the sum,
#and check if the last digit equals the sum modulo of 10
def PosCode (userInput):
    newStr = userInput[:-1]
    lastDigit = int(userInput[-1])
    total = 0
    for i in range(len(newStr)):
        total = total + int(userInput[i])*(i+1)
    remain = total % 10
    if lastDigit == remain:
        pos = True
    else:
        pos = False
    return pos
#function removes the last digit, multiplies each odd position by 3 and even position by 1, modulo 10 the sum,
#and check if the last digit is equal to 10 - sum of modulo 10 if the value is not 0
def UPC (userInput):
    newStr = userInput[:-1]
    lastDigit = int(userInput[-1])
    total = 0
    for i in range(len(newStr)):
        curDig = int(userInput[i])
        if ((i+1) % 2) != 0:
            curDig = curDig*3
        total = total + curDig
    remain = total % 10
    finalTotal = 10 - remain
    if finalTotal != 10:
        if lastDigit == finalTotal:
            upc = True
        else:
            upc = False
    else:
        if lastDigit == remain:
            upc = True
        else:
            upc = False
    return upc

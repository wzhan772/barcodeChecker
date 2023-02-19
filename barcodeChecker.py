'''
Take a user's integer input and call each code check function (basic, positional, and upc)
Stop when the user enters 0
Created by: William Zhang, CS1026A
Student ID: 251215208
'''
#import functions from code_check.py
from code_check import BasicCode, PosCode, UPC
#create empty lists
BasicList = []
PosList = []
UPCList = []
NoneList = []
#while loop to ask user for integer until 0 is entered
done = False
while not done:
    code = input("Please enter code (digits only) (enter 0 to quit)")
    if int(code) == 0:
        done = True
    else:
        #call each function to determine if code is valid or not
        BasicCheck = BasicCode(code)
        PosCheck = PosCode(code)
        UPCCheck = UPC(code)
        #if each code is valid, add it to its respective list
        if BasicCheck == True:
            print("-- code:", code + " valid Basic code.")
            BasicList.append(code)
        if PosCheck == True:
            print("-- code:", code + " valid Position code.")
            PosList.append(code)
        if UPCCheck == True:
            print("-- code:", code + " valid UPC code.")
            UPCList.append(code)
        #if the code is not valid for any list, add it to the 'none' list
        if BasicCheck == False and PosCheck == False and UPCCheck == False:
            print("-- code:", code + " not Basic, Position, or UPC code.")
            NoneList.append(code)
#if there are no values in the list, print out 'none'
if not BasicList:
    BasicList.append("None")
if not PosList:
    PosList.append("None")
if not UPCList:
    UPCList.append("None")
if not NoneList:
    NoneList.append("None")
#empty strings to concatenate
BaseStr = ""
PosStr = ""
UPCStr = ""
NoneStr = ""
#loop through each list and add each value into the empty corresponding string
for i in range(len(BasicList)):
    BaseStr += BasicList[i] + ", "
for i in range(len(PosList)):
    PosStr += PosList[i] + ", "
for i in range(len(UPCList)):
    UPCStr += UPCList[i] + ", "
for i in range(len(NoneList)):
    NoneStr += NoneList[i] + ", "
#print out the summary
print("Summary\n"+"Basic :",BaseStr[:-2], "\n"+"Position :",PosStr[:-2],"\n"+"UPC :",UPCStr[:-2],"\n"+"None :",NoneStr[:-2])

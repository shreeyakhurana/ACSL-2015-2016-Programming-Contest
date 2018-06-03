"""
Takoma Park M.S
Jr-5
Contest 1
Shreeya Khurana
"""
print("This is a Python program")
print("Enter the inputs as a string of 3 octal digits")
print("each seperated by a comma without spaces (1,2,3)")
print("between the comma")
##Receive Inputs##
octal1 = input("1. ")
octal2 = input("2. ")
octal3 = input("3. ")
octal4 = input("4. ")
octal5 = input("5. ")

##Convert to octal to decimal##
octal1_split = octal1.split(',')
octal1_split = [int(n) for n in octal1_split]

octal2_split = octal2.split(',')
octal2_split = [int(n) for n in octal2_split]

octal3_split = octal3.split(',')
octal3_split = [int(n) for n in octal3_split]

octal4_split = octal4.split(',')
octal4_split = [int(n) for n in octal4_split]

octal5_split = octal5.split(',')
octal5_split = [int(n) for n in octal5_split]



decimal1 = int(int(octal1_split[2]) + int(8*octal1_split[1]) + int(64*octal1_split[0]))
decimal2 = int(int(octal2_split[2]) + int(8*octal2_split[1]) + int(64*octal2_split[0]))
decimal3 = int(int(octal3_split[2]) + int(8*octal3_split[1]) + int(64*octal3_split[0]))
decimal4 = int(int(octal4_split[2]) + int(8*octal4_split[1]) + int(64*octal4_split[0]))
decimal5 = int(int(octal5_split[2]) + int(8*octal5_split[1]) + int(64*octal5_split[0]))



##Convert decimal to binary##

#first number#
binary1 = "{0:b}".format(decimal1)


#second number#
binary2 = "{0:b}".format(decimal2)

#third number#
binary3 = "{0:b}".format(decimal3)

#fourth number#
binary4 = "{0:b}".format(decimal4)

#fifth number#
binary5 = "{0:b}".format(decimal5)



##Convert binary to CHMOD##
binary1 = list(binary1)
binary2 = list(binary2)
binary3 = list(binary3)
binary4 = list(binary4)
binary5 = list(binary5)


def createList(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n
        
createList(binary1)
createList(binary2)
createList(binary3)
createList(binary4)
createList(binary5)

def createListagain(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createListagain(binary1)
createListagain(binary2)
createListagain(binary3)
createListagain(binary4)
createListagain(binary5)

def createList1(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList1(binary1)
createList1(binary2)
createList1(binary3)
createList1(binary4)
createList1(binary5)

def createList2(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList2(binary1)
createList2(binary2)
createList2(binary3)
createList2(binary4)
createList2(binary5)

def createList3(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList3(binary1)
createList3(binary2)
createList3(binary3)
createList3(binary4)
createList3(binary5)

def createList4(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList4(binary1)
createList4(binary2)
createList4(binary3)
createList4(binary4)
createList4(binary5)

def createList5(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList5(binary1)
createList5(binary2)
createList5(binary3)
createList5(binary4)
createList5(binary5)

def createList6(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList6(binary1)
createList6(binary2)
createList6(binary3)
createList6(binary4)
createList6(binary5)

def createList7(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createList7(binary1)
createList7(binary2)
createList7(binary3)
createList7(binary4)
createList7(binary5)

def CHMOD(LIST):
    global CHMOD0
    global CHMOD1
    global CHMOD2
    global CHMOD3
    global CHMOD4
    global CHMOD5
    global CHMOD6
    global CHMOD7
    global CHMOD8
    if LIST[0] == '1':
        CHMOD0 = "r"
    else:
        CHMOD0 = "-"

    if LIST[1] == '1':
        CHMOD1 = "w"
    else:
        CHMOD1 = "-"

    if LIST[2] == '1':
        CHMOD2 = "x"
    else:
        CHMOD2 = "-"

    if LIST[3] == '1':
        CHMOD3 = "r"
    else:
        CHMOD3 = "-"

    if LIST[4] == '1':
        CHMOD4 = "w"
    else:
        CHMOD4 = "-"

    if LIST[5] == '1':
        CHMOD5 = "x"
    else:
        CHMOD5 = "-"

    if LIST[6] == '1':
        CHMOD6 = "r"
    else:
        CHMOD6 = "-"

    if LIST[7] == '1':
        CHMOD7 = "w"
    else:
        CHMOD7 = "-"

    if LIST[8] == '1':
        CHMOD8 = "x"
    else:
        CHMOD8 = "-"


CHMOD(binary1)
CHMODLIST1_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODLIST1_2 = CHMOD3 + CHMOD4 + CHMOD5
CHMODLIST1_3 = CHMOD6 + CHMOD7 + CHMOD8

CHMOD(binary2)
CHMODLIST2_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODLIST2_2 = CHMOD3 + CHMOD4 + CHMOD5
CHMODLIST2_3 = CHMOD6 + CHMOD7 + CHMOD8

CHMOD(binary3)
CHMODLIST3_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODLIST3_2 = CHMOD3 + CHMOD4 + CHMOD5
CHMODLIST3_3 = CHMOD6 + CHMOD7 + CHMOD8

CHMOD(binary4)
CHMODLIST4_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODLIST4_2 = CHMOD3 + CHMOD4 + CHMOD5
CHMODLIST4_3 = CHMOD6 + CHMOD7 + CHMOD8

CHMOD(binary5)
CHMODLIST5_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODLIST5_2 = CHMOD3 + CHMOD4 + CHMOD5
CHMODLIST5_3 = CHMOD6 + CHMOD7 + CHMOD8

CHMODLIST1_1_list = list(CHMODLIST1_1)
CHMODLIST1_2_list = list(CHMODLIST1_2)
CHMODLIST1_3_list = list(CHMODLIST1_3)
CHMODLIST2_1_list = list(CHMODLIST2_1)
CHMODLIST2_2_list = list(CHMODLIST2_2)
CHMODLIST2_3_list = list(CHMODLIST2_3)
CHMODLIST3_1_list = list(CHMODLIST3_1)
CHMODLIST3_2_list = list(CHMODLIST3_2)
CHMODLIST3_3_list = list(CHMODLIST3_3)
CHMODLIST4_1_list = list(CHMODLIST4_1)
CHMODLIST4_2_list = list(CHMODLIST4_2)
CHMODLIST4_3_list = list(CHMODLIST4_3)
CHMODLIST5_1_list = list(CHMODLIST5_1)
CHMODLIST5_2_list = list(CHMODLIST5_2)
CHMODLIST5_3_list = list(CHMODLIST5_3)


def CHMODagain(LIST):
    global bin0
    global bin1
    global bin2
    if LIST[0] == 'r':
        bin0 = "1"
    else:
        bin0 = "0"

    if LIST[1] == 'w':
        bin1 = "1"
    else:
        bin1 = "0"

    if LIST[2] == 'x':
        bin2 = "1"
    else:
        bin2 = "0"
CHMODagain(CHMODLIST1_1_list)
binlist1 = bin0 + bin1 + bin2


CHMODagain(CHMODLIST1_2_list)
binlist2 = bin0 + bin1 + bin2


CHMODagain(CHMODLIST1_3_list)
binlist3 = bin0 + bin1 + bin2


CHMODagain(CHMODLIST2_1_list)
binlist4 = bin0 + bin1 + bin2


CHMODagain(CHMODLIST2_2_list)
binlist5 = bin0 + bin1 + bin2


CHMODagain(CHMODLIST2_3_list)
binlist6 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST3_1_list)
binlist7 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST3_2_list)
binlist8 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST3_3_list)
binlist9 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST4_1_list)
binlist10 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST4_2_list)
binlist11 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST4_3_list)
binlist12 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST5_1_list)
binlist13 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST5_2_list)
binlist14 = bin0 + bin1 + bin2

CHMODagain(CHMODLIST5_3_list)
binlist15 = bin0 + bin1 + bin2
    

##Printing Outputs##
print()
print()
print()
print("1. ",binlist1, binlist2, binlist3, "and ", CHMODLIST1_1, CHMODLIST1_2, CHMODLIST1_3)
print("2. ",binlist4, binlist5, binlist6, "and ", CHMODLIST2_1, CHMODLIST2_2, CHMODLIST2_3)
print("3. ",binlist7, binlist8, binlist9, "and ", CHMODLIST3_1, CHMODLIST3_2, CHMODLIST3_3)
print("4. ",binlist10, binlist11, binlist12, "and ", CHMODLIST4_1, CHMODLIST4_2, CHMODLIST4_3)
print("5. ",binlist13, binlist14, binlist15, "and ", CHMODLIST5_1, CHMODLIST5_2, CHMODLIST5_3)

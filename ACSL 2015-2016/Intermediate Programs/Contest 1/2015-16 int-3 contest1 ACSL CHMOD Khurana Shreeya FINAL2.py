"""
Int-3
Contest 1
Shreeya Khurana
"""
print("This is a Python program")
print("Enter the inputs as a string of 3 digits")
print("the first 2 should be octal strings (1,2,3)")
print("the second 2 should be binary strings (100,001,101)")
print("and the last should be UNIX string (rwx,-wx,-wx)")
print("each seperated by a comma without spaces")
print("between the comma")

##Receive Inputs##
octal1 = input("1. ")
octal2 = input("2. ")
binary3 = input("3. ")
binary4 = input("4. ")
UNIX5 = input("5. ")

##Convert to octal to decimal##

octal1_split = octal1.split(',')
octal1_split = [int(n) for n in octal1_split]

octal2_split = octal2.split(',')
octal2_split = [int(n) for n in octal2_split]

decimal1 = int(int(octal1_split[2]) + int(8*octal1_split[1]) + int(64*octal1_split[0]))
decimal2 = int(int(octal2_split[2]) + int(8*octal2_split[1]) + int(64*octal2_split[0]))

##Convert octal to binary##

#first number#
binary1 = "{0:b}".format(decimal1)

#second number#
binary2 = "{0:b}".format(decimal2)

##Convert binary to UNIX##
binary1 = list(binary1)
binary2 = list(binary2)

def createList(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n
        
createList(binary1)
createList(binary2)


def createListagain(n):
    if len(n) < 9:
        n = n.insert(0, str(0))
    elif len(n) == 9:
        n = n

createListagain(binary1)
createListagain(binary2)


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


CHMODLIST1_1_list = list(CHMODLIST1_1)
CHMODLIST1_2_list = list(CHMODLIST1_2)
CHMODLIST1_3_list = list(CHMODLIST1_3)
CHMODLIST2_1_list = list(CHMODLIST2_1)
CHMODLIST2_2_list = list(CHMODLIST2_2)
CHMODLIST2_3_list = list(CHMODLIST2_3)

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




###################################################

##Convert binary to decimal##

binary3_split = binary3.split(',')
binary3_split = [str(n)for n in binary3_split]

binary3_1, binary3_2, binary3_3 = binary3_split


binary4_split = binary4.split(',')
binary4_split = [str(n) for n in binary4_split]

binary4_1, binary4_2, binary4_3 = binary4_split


decimal3_1 = 0
for digit in binary3_1:
    decimal3_1 = decimal3_1*2 + int(digit)

decimal3_2 = 0
for digit in binary3_2:
    decimal3_2 = decimal3_2*2 + int(digit)

decimal3_3 = 0
for digit in binary3_3:
    decimal3_3 = decimal3_3*2 + int(digit)

decimal3_1 = str(decimal3_1)
decimal3_2 = str(decimal3_2)
decimal3_3 = str(decimal3_3)

decimal3 = decimal3_1 + decimal3_2 + decimal3_3

decimal4_1 = 0
for digit in binary4_1:
    decimal4_1 = decimal4_1*2 + int(digit)

decimal4_2 = 0
for digit in binary4_2:
    decimal4_2 = decimal4_2*2 + int(digit)

decimal4_3 = 0
for digit in binary4_3:
    decimal4_3 = decimal4_3*2 + int(digit)

decimal4_1 = str(decimal4_1)
decimal4_2 = str(decimal4_2)
decimal4_3 = str(decimal4_3)

decimal4 = decimal4_1 + decimal4_2 + decimal4_3
##Convert decimal to octal##
octal3 = decimal3
octal4 = decimal4



##Convert octal to UNIX (using binary)##
def CHMODsmall(LIST):
    global CHMOD0
    global CHMOD1
    global CHMOD2
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


CHMODsmall(binary3_1)
CHMODLIST3_1 = CHMOD0 + CHMOD1 + CHMOD2

CHMODsmall(binary3_2)
CHMODLIST3_2 = CHMOD0 + CHMOD1 + CHMOD2
CHMODsmall(binary3_3)

CHMODLIST3_3 = CHMOD0 + CHMOD1 + CHMOD2



CHMODsmall(binary4_1)
CHMODLIST4_1 = CHMOD0 + CHMOD1 + CHMOD2
CHMODsmall(binary4_2)

CHMODLIST4_2 = CHMOD0 + CHMOD1 + CHMOD2
CHMODsmall(binary4_3)

CHMODLIST4_3 = CHMOD0 + CHMOD1 + CHMOD2


CHMODLIST3_1_list = list(CHMODLIST3_1)
CHMODLIST3_2_list = list(CHMODLIST3_2)
CHMODLIST3_3_list = list(CHMODLIST3_3)
CHMODLIST4_1_list = list(CHMODLIST4_1)
CHMODLIST4_2_list = list(CHMODLIST4_2)
CHMODLIST4_3_list = list(CHMODLIST4_3)

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

##############################################################

##Convert UNIX to binary##
UNIX5_split =UNIX5.split(',')
UNIX5_split = [str(n) for n in UNIX5_split]

UNIX5_1_1, UNIX5_2_1, UNIX5_3_1 = UNIX5_split

UNIX5_1_1 = list(UNIX5_1_1)
UNIX5_2_1 = list(UNIX5_2_1)
UNIX5_3_1 = list(UNIX5_3_1)

def UNIX(LIST):
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

    

UNIX(UNIX5_1_1)
UNIXLIST5_1 = bin0 + bin1 + bin2
UNIX(UNIX5_2_1)
UNIXLIST5_2 = bin0 + bin1 + bin2
UNIX(UNIX5_3_1)
UNIXLIST5_3 = bin0 + bin1 + bin2


##Convert UNIX to Octal (using binary)##
decimal5_1 = 0
for digit in UNIXLIST5_1:
    decimal5_1 = decimal5_1*2 + int(digit)

decimal5_2 = 0
for digit in UNIXLIST5_2:
    decimal5_2 = decimal5_2*2 + int(digit)

decimal5_3 = 0
for digit in UNIXLIST5_3:
    decimal5_3 = decimal5_3*2 + int(digit)

decimal5_1 = str(decimal5_1)
decimal5_2 = str(decimal5_2)
decimal5_3 = str(decimal5_3)

decimal5 = decimal5_1 + decimal5_2 + decimal5_3
UNIXoctal = decimal5
#################################################

##Printing Outputs##
print()
print()
print()
print("1.",binlist1, binlist2, binlist3,"and", CHMODLIST1_1, CHMODLIST1_2, CHMODLIST1_3)
print("2.",binlist4, binlist5, binlist6,"and", CHMODLIST2_1, CHMODLIST2_2, CHMODLIST2_3)
print("3.",octal3, "and", CHMODLIST3_1, CHMODLIST3_2, CHMODLIST3_3)
print("4.",octal4, "and", CHMODLIST4_1, CHMODLIST4_2, CHMODLIST4_3)
print("5.",UNIXoctal, "and", UNIXLIST5_1, UNIXLIST5_2, UNIXLIST5_3)

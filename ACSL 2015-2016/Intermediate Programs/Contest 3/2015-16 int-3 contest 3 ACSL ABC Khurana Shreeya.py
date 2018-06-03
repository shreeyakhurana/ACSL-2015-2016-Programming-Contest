"""
Takoma Park M.S.
Int-3
Contest 3
Shreeya Khurana
"""
print("""Please input your values separated by COMMAS WITH SPACES AFTER
(For example, the first input could be 9, 17, 22, 26, 4, A, 7, C, 18, C, 19, C, 32, 14.) 
The output will be displayed after entering each input.
""")
input1 = input("1. ")
"""
input2 = input("2. ")
input3 = input("3. ")
input4 = input("4. ")
input5 = input("5. ")
"""
input1_split = input1.split(", ")
"""
input3 = input("3. ")

input3_split = input3.split(", ")
input4_split = input4.split(", ")
input5_split = input5.split(", ")
"""


####For Input1###
row1_1 = ["0", "0", "0", "0", "0", "0"]
row2_1 = ["0", "0", "0", "0", "0", "0"]
row3_1 = ["0", "0", "0", "0", "0", "0"]
row4_1 = ["0", "0", "0", "0", "0", "0"]
row5_1 = ["0", "0", "0", "0", "0", "0"]
row6_1 = ["0", "0", "0", "0", "0", "0"]

assign1 = int(input1_split[0])
assign2 = int(input1_split[1])
assign3 = int(input1_split[2])
assign4 = int(input1_split[3])

fulltable = [row1_1, row2_1, row3_1, row4_1, row5_1, row6_1]
##fill in filler stuff##
def assignfill(assign1):
    placer1 = 0
    placec1 = 0
    if assign1//6 == assign1/6:
        placer1 = (assign1//6)-1
    else:
        placer1 = assign1//6
    placec1 = assign1 % 6
    placec1 = placec1 - 1

    fulltable[placer1][placec1] = 'D'

assignfill(assign1)
assignfill(assign2)
assignfill(assign3)
assignfill(assign4)

input1_split = input1_split[5: len(input1_split)]

location1 = int(input1_split.pop(len(input1_split)-1))


##fill in letters##
index = 0
location_list = []
letter_list = []
while index < len(input1_split):
    if index % 2 == 0:
        letter = input1_split[index]
        letter_list.append(letter)
    else:
        location = input1_split[index]
        location_list.append(location)        
    index +=1
###Top row###
index = 0
while index < len(letter_list):
    letter = letter_list[index]
    if int(location_list[index]) == 2:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[2][1] = letter
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 3:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][2] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[1][2] = letter
        index +=1
    elif int(location_list[index]) == 4:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][3] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[1][3] = letter
        index +=1
    elif int(location_list[index]) == 5:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[2][4] = letter             
        else:
            fulltable[1][3] = letter
        index +=1
    ###Side column###
    elif int(location_list[index]) == 7:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[1][2] = letter             
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 13:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][1] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[2][1] = letter
        index +=1
    elif int(location_list[index]) == 19:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][1] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[3][1] = letter
        index +=1
    elif int(location_list[index]) == 25:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[4][2] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    ##Bottom Row##
    elif int(location_list[index]) == 32:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[3][1] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    elif int(location_list[index]) == 33:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][2] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[4][2] = letter
        index +=1
    elif int(location_list[index]) == 34:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][3] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[4][3] = letter
        index +=1
    elif int(location_list[index]) == 35:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[3][4] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    ##Side column##
    elif int(location_list[index]) == 30:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[4][3] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    elif int(location_list[index]) == 24:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][4] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[3][4] = letter
        index +=1
    elif int(location_list[index]) == 18:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][4] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[2][4] = letter
        index +=1
    elif int(location_list[index]) == 12:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[1][3] = letter
        else:
            fulltable[1][4] = letter
        index +=1
row1_2 = row2_1[1:5]
row2_2 = row3_1[1:5]
row3_2 = row4_1[1:5]
row4_2 = row5_1[1:5]
newtable = [row1_2, row2_2, row3_2, row4_2]
column1 = [row[0] for row in newtable]
column2 = [row[1] for row in newtable]
column3 = [row[2] for row in newtable]
column4 = [row[3] for row in newtable]
list_columns = [column1, column2, column3, column4]
totalrows = row1_2 + row2_2 + row3_2 + row4_2
count1 = totalrows.count("0")
count1r = row1_2.count("0")
count2r = row2_2.count("0")
count3r = row3_2.count("0")
count4r = row4_2.count("0")
countc1 = column1.count("0")
countc2 = column2.count("0")
countc3 = column3.count("0")
countc4 = column4.count("0")
for i in range(25):
    for row in newtable:
        countr = row.count('0')
        if countr == 1:
            index = row.index('0')
            if 'A' not in row:
                row[index] = 'A'
            elif 'B' not in row:
                row[index] = 'B'
            elif 'C' not in row:
                row[index] = 'C'

    countc1 = column1.count('0')
    if countc1 == 1:
        index1 = column1.index('0')
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'
            
        countc2 = column2.count('0')
        if countc2 == 1:
            index2 = column2.index('0')
            if 'A' not in column2:
                newtable[index2][1] = 'A'
            elif 'B' not in column2:
                newtable[index2][1] = 'B'
            elif 'C' not in column2:
                newtable[index2][1] = 'C'
            elif 'D' not in column2:
                newtable[index2][1] = 'D'
        countc3 = column3.count('0')
        if countc3 == 1:
            index3 = column3.index('0')
            if 'A' not in column3:
                newtable[index3][2] = 'A'
            elif 'B' not in column3:
                newtable[index3][2] = 'B'
            elif 'C' not in column3:
                newtable[index3][2] = 'C'
            elif 'D' not in column3:
                newtable[index3][2] = 'D'
        countc4 = column4.count('0')
        if countc4 == 1:
            index4 = column4.index('0')
            if 'A' not in column4:
                newtable[index4][3] = 'A'
            elif 'B' not in column4:
                newtable[index4][3] = 'B'
            elif 'C' not in column4:
                newtable[index4][3] = 'C'
            elif 'D' not in column4:
                newtable[index4][2] = 'D'
        i+=1


          #####
    countr1 = row1_2.count('0')
    if countr1 == 2:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' in row1_2:
            row1_2[index] = 'B'
        elif 'B' in row1_2 or 'C' in row1_2:
            row1_2[index] = 'A'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr2 = row2_2.count('0')
    if countr2 == 2:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr3 = row3_2.count('0')
    if countr3 == 2:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr4 = row4_2.count('0')
    if countr4 == 2:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]
        #Loop the 1 0 loop again
    for i in range(25):
        for row in newtable:
            countr = row.count('0')
            if countr == 1:
                index = row.index('0')
                if 'A' not in row:
                    row[index] = 'A'
                elif 'B' not in row:
                    row[index] = 'B'
                elif 'C' not in row:
                    row[index] = 'C'

        countc1 = column1.count('0')
        if countc1 == 1:
            index1 = column1.index('0')
            if 'A' not in column1:
                newtable[index1][0] = 'A'
            elif 'B' not in column1:
                newtable[index1][0] = 'B'
            elif 'C' not in column1:
                newtable[index1][0] = 'C'
            elif 'D' not in column1:
                newtable[index1][0] = 'D'
                
            countc2 = column2.count('0')
            if countc2 == 1:
                index2 = column2.index('0')
                if 'A' not in column2:
                    newtable[index2][1] = 'A'
                elif 'B' not in column2:
                    newtable[index2][1] = 'B'
                elif 'C' not in column2:
                    newtable[index2][1] = 'C'
                elif 'D' not in column2:
                    newtable[index2][1] = 'D'
            countc3 = column3.count('0')
            if countc3 == 1:
                index3 = column3.index('0')
                if 'A' not in column3:
                    newtable[index3][2] = 'A'
                elif 'B' not in column3:
                    newtable[index3][2] = 'B'
                elif 'C' not in column3:
                    newtable[index3][2] = 'C'
                elif 'D' not in column3:
                    newtable[index3][2] = 'D'
            countc4 = column4.count('0')
            if countc4 == 1:
                index4 = column4.index('0')
                if 'A' not in column4:
                    newtable[index4][3] = 'A'
                elif 'B' not in column4:
                    newtable[index4][3] = 'B'
                elif 'C' not in column4:
                    newtable[index4][3] = 'C'
                elif 'D' not in column4:
                    newtable[index4][2] = 'D'
            i+=1

    column1 = [row[0] for row in newtable]
    countc1 = column1.count('0')
    if countc1 == 2:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    column2 = [row[1] for row in newtable]
    countc2 = column2.count('0')
    if countc2 == 2:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    column3 = [row[2] for row in newtable]
    countc3 = column3.count('0')
    if countc3 == 2:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    column4 = [row[3] for row in newtable]
    countc4 = column4.count('0')
    if countc4 == 2:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column4 = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    countr1 = row1_2.count('0')
    if countr1 == 3:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' not in row1_2:
            row1_2[index] = 'A'
        elif 'B' not in row1_2:
            row1_2[index] = 'B'
        elif 'C' not in row1_2:
            row1_2[index] = 'C'
        elif 'D' not in row1_2:
            row1_2[index] = 'D'

    countr2 = row2_2.count('0')
    if countr2 == 3:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'

    countr3 = row3_2.count('0')
    if countr3 == 3:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'

    countr4 = row4_2.count('0')
    if countr4 == 3:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'

    countc1 = column1.count('0')
    if countc1 == 3:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    countc2 = column2.count('0')
    if countc2 == 3:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    countc3 = column3.count('0')
    if countc3 == 3:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    countc4 = column4.count('0')
    if countc4 == 3:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    if location1 == 8:
        letter = newtable[0][0]
    elif location1 == 9:
        letter = newtable[0][1]
    elif location1 == 10:
        letter = newtable[0][2]
    elif location1 == 11:
        letter = newtable[0][3]
    elif location1 == 14:
        letter = newtable[1][0]
    elif location1 == 15:
        letter = newtable[1][1]
    elif location1 == 16:
        letter = newtable[1][2]
    elif location1 == 17:
        letter = newtable[1][3]
    elif location1 == 20:
        letter = newtable[2][0]
    elif location1 == 21:
        letter = newtable[2][1]
    elif location1 == 22:
        letter = newtable[2][2]
    elif location1 == 23:
        letter = newtable[2][3]
    elif location1 == 26:
        letter = newtable[3][0]
    elif location1 == 27:
        letter = newtable[3][1]
    elif location1 == 28:
        letter = newtable[3][2]
    elif location1 == 29:
        letter = newtable[3][3]
        
print("1. ", letter)
        
input2 = input("2. ")
input2_split = input2.split(", ")
row1_1 = ["0", "0", "0", "0", "0", "0"]
row2_1 = ["0", "0", "0", "0", "0", "0"]
row3_1 = ["0", "0", "0", "0", "0", "0"]
row4_1 = ["0", "0", "0", "0", "0", "0"]
row5_1 = ["0", "0", "0", "0", "0", "0"]
row6_1 = ["0", "0", "0", "0", "0", "0"]


assign1 = int(input2_split[0])
assign2 = int(input2_split[1])
assign3 = int(input2_split[2])
assign4 = int(input2_split[3])

fulltable = [row1_1, row2_1, row3_1, row4_1, row5_1, row6_1]
##fill in filler stuff##
def assignfill(assign1):
    placer1 = 0
    placec1 = 0
    if assign1//6 == assign1/6:
        placer1 = (assign1//6)-1
    else:
        placer1 = assign1//6
    placec1 = assign1 % 6
    placec1 = placec1 - 1

    fulltable[placer1][placec1] = 'D'

assignfill(assign1)
assignfill(assign2)
assignfill(assign3)
assignfill(assign4)

input2_split = input2_split[5: len(input2_split)]

location1 = int(input2_split.pop(len(input2_split)-1))


##fill in letters##
index = 0
location_list = []
letter_list = []
while index < len(input2_split):
    if index % 2 == 0:
        letter = input2_split[index]
        letter_list.append(letter)
    else:
        location = input2_split[index]
        location_list.append(location)        
    index +=1
###Top row###
index = 0
while index < len(letter_list):
    letter = letter_list[index]
    if int(location_list[index]) == 2:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[2][1] = letter
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 3:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][2] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[1][2] = letter
        index +=1
    elif int(location_list[index]) == 4:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][3] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[1][3] = letter
        index +=1
    elif int(location_list[index]) == 5:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[2][4] = letter             
        else:
            fulltable[1][3] = letter
        index +=1
    ###Side column###
    elif int(location_list[index]) == 7:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[1][2] = letter             
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 13:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][1] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[2][1] = letter
        index +=1
    elif int(location_list[index]) == 19:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][1] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[3][1] = letter
        index +=1
    elif int(location_list[index]) == 25:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[4][2] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    ##Bottom Row##
    elif int(location_list[index]) == 32:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[3][1] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    elif int(location_list[index]) == 33:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][2] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[4][2] = letter
        index +=1
    elif int(location_list[index]) == 34:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][3] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[4][3] = letter
        index +=1
    elif int(location_list[index]) == 35:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[3][4] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    ##Side column##
    elif int(location_list[index]) == 30:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[4][3] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    elif int(location_list[index]) == 24:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][4] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[3][4] = letter
        index +=1
    elif int(location_list[index]) == 18:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][4] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[2][4] = letter
        index +=1
    elif int(location_list[index]) == 12:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[1][3] = letter
        else:
            fulltable[1][4] = letter
        index +=1
row1_2 = row2_1[1:5]
row2_2 = row3_1[1:5]
row3_2 = row4_1[1:5]
row4_2 = row5_1[1:5]
newtable = [row1_2, row2_2, row3_2, row4_2]
column1 = [row[0] for row in newtable]
column2 = [row[1] for row in newtable]
column3 = [row[2] for row in newtable]
column4 = [row[3] for row in newtable]
list_columns = [column1, column2, column3, column4]
totalrows = row1_2 + row2_2 + row3_2 + row4_2
count1 = totalrows.count("0")
count1r = row1_2.count("0")
count2r = row2_2.count("0")
count3r = row3_2.count("0")
count4r = row4_2.count("0")
countc1 = column1.count("0")
countc2 = column2.count("0")
countc3 = column3.count("0")
countc4 = column4.count("0")
for i in range(25):
    for row in newtable:
        countr = row.count('0')
        if countr == 1:
            index = row.index('0')
            if 'A' not in row:
                row[index] = 'A'
            elif 'B' not in row:
                row[index] = 'B'
            elif 'C' not in row:
                row[index] = 'C'

    countc1 = column1.count('0')
    if countc1 == 1:
        index1 = column1.index('0')
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'
            
        countc2 = column2.count('0')
        if countc2 == 1:
            index2 = column2.index('0')
            if 'A' not in column2:
                newtable[index2][1] = 'A'
            elif 'B' not in column2:
                newtable[index2][1] = 'B'
            elif 'C' not in column2:
                newtable[index2][1] = 'C'
            elif 'D' not in column2:
                newtable[index2][1] = 'D'
        countc3 = column3.count('0')
        if countc3 == 1:
            index3 = column3.index('0')
            if 'A' not in column3:
                newtable[index3][2] = 'A'
            elif 'B' not in column3:
                newtable[index3][2] = 'B'
            elif 'C' not in column3:
                newtable[index3][2] = 'C'
            elif 'D' not in column3:
                newtable[index3][2] = 'D'
        countc4 = column4.count('0')
        if countc4 == 1:
            index4 = column4.index('0')
            if 'A' not in column4:
                newtable[index4][3] = 'A'
            elif 'B' not in column4:
                newtable[index4][3] = 'B'
            elif 'C' not in column4:
                newtable[index4][3] = 'C'
            elif 'D' not in column4:
                newtable[index4][2] = 'D'
        i+=1


          #####
    countr1 = row1_2.count('0')
    if countr1 == 2:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' in row1_2:
            row1_2[index] = 'B'
        elif 'B' in row1_2 or 'C' in row1_2:
            row1_2[index] = 'A'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr2 = row2_2.count('0')
    if countr2 == 2:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr3 = row3_2.count('0')
    if countr3 == 2:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr4 = row4_2.count('0')
    if countr4 == 2:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]
        #Loop the 1 0 loop again
    for i in range(25):
        for row in newtable:
            countr = row.count('0')
            if countr == 1:
                index = row.index('0')
                if 'A' not in row:
                    row[index] = 'A'
                elif 'B' not in row:
                    row[index] = 'B'
                elif 'C' not in row:
                    row[index] = 'C'

        countc1 = column1.count('0')
        if countc1 == 1:
            index1 = column1.index('0')
            if 'A' not in column1:
                newtable[index1][0] = 'A'
            elif 'B' not in column1:
                newtable[index1][0] = 'B'
            elif 'C' not in column1:
                newtable[index1][0] = 'C'
            elif 'D' not in column1:
                newtable[index1][0] = 'D'
                
            countc2 = column2.count('0')
            if countc2 == 1:
                index2 = column2.index('0')
                if 'A' not in column2:
                    newtable[index2][1] = 'A'
                elif 'B' not in column2:
                    newtable[index2][1] = 'B'
                elif 'C' not in column2:
                    newtable[index2][1] = 'C'
                elif 'D' not in column2:
                    newtable[index2][1] = 'D'
            countc3 = column3.count('0')
            if countc3 == 1:
                index3 = column3.index('0')
                if 'A' not in column3:
                    newtable[index3][2] = 'A'
                elif 'B' not in column3:
                    newtable[index3][2] = 'B'
                elif 'C' not in column3:
                    newtable[index3][2] = 'C'
                elif 'D' not in column3:
                    newtable[index3][2] = 'D'
            countc4 = column4.count('0')
            if countc4 == 1:
                index4 = column4.index('0')
                if 'A' not in column4:
                    newtable[index4][3] = 'A'
                elif 'B' not in column4:
                    newtable[index4][3] = 'B'
                elif 'C' not in column4:
                    newtable[index4][3] = 'C'
                elif 'D' not in column4:
                    newtable[index4][2] = 'D'
            i+=1

    column1 = [row[0] for row in newtable]
    countc1 = column1.count('0')
    if countc1 == 2:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    column2 = [row[1] for row in newtable]
    countc2 = column2.count('0')
    if countc2 == 2:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    column3 = [row[2] for row in newtable]
    countc3 = column3.count('0')
    if countc3 == 2:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    column4 = [row[3] for row in newtable]
    countc4 = column4.count('0')
    if countc4 == 2:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column4 = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    countr1 = row1_2.count('0')
    if countr1 == 3:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' not in row1_2:
            row1_2[index] = 'A'
        elif 'B' not in row1_2:
            row1_2[index] = 'B'
        elif 'C' not in row1_2:
            row1_2[index] = 'C'
        elif 'D' not in row1_2:
            row1_2[index] = 'D'

    countr2 = row2_2.count('0')
    if countr2 == 3:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'

    countr3 = row3_2.count('0')
    if countr3 == 3:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'

    countr4 = row4_2.count('0')
    if countr4 == 3:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'

    countc1 = column1.count('0')
    if countc1 == 3:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    countc2 = column2.count('0')
    if countc2 == 3:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    countc3 = column3.count('0')
    if countc3 == 3:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    countc4 = column4.count('0')
    if countc4 == 3:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    if location1 == 8:
        letter = newtable[0][0]
    elif location1 == 9:
        letter = newtable[0][1]
    elif location1 == 10:
        letter = newtable[0][2]
    elif location1 == 11:
        letter = newtable[0][3]
    elif location1 == 14:
        letter = newtable[1][0]
    elif location1 == 15:
        letter = newtable[1][1]
    elif location1 == 16:
        letter = newtable[1][2]
    elif location1 == 17:
        letter = newtable[1][3]
    elif location1 == 20:
        letter = newtable[2][0]
    elif location1 == 21:
        letter = newtable[2][1]
    elif location1 == 22:
        letter = newtable[2][2]
    elif location1 == 23:
        letter = newtable[2][3]
    elif location1 == 26:
        letter = newtable[3][0]
    elif location1 == 27:
        letter = newtable[3][1]
    elif location1 == 28:
        letter = newtable[3][2]
    elif location1 == 29:
        letter = newtable[3][3]
print("2. ", letter)        

input3 = input("3. ")

input3_split = input3.split(", ")
row1_1 = ["0", "0", "0", "0", "0", "0"]
row2_1 = ["0", "0", "0", "0", "0", "0"]
row3_1 = ["0", "0", "0", "0", "0", "0"]
row4_1 = ["0", "0", "0", "0", "0", "0"]
row5_1 = ["0", "0", "0", "0", "0", "0"]
row6_1 = ["0", "0", "0", "0", "0", "0"]

assign1 = int(input3_split[0])
assign2 = int(input3_split[1])
assign3 = int(input3_split[2])
assign4 = int(input3_split[3])

fulltable = [row1_1, row2_1, row3_1, row4_1, row5_1, row6_1]
##fill in filler stuff##
def assignfill(assign1):
    placer1 = 0
    placec1 = 0
    if assign1//6 == assign1/6:
        placer1 = (assign1//6)-1
    else:
        placer1 = assign1//6
    placec1 = assign1 % 6
    placec1 = placec1 - 1

    fulltable[placer1][placec1] = 'D'

assignfill(assign1)
assignfill(assign2)
assignfill(assign3)
assignfill(assign4)

input3_split = input3_split[5: len(input3_split)]

location1 = int(input3_split.pop(len(input3_split)-1))


##fill in letters##
index = 0
location_list = []
letter_list = []
while index < len(input3_split):
    if index % 2 == 0:
        letter = input3_split[index]
        letter_list.append(letter)
    else:
        location = input3_split[index]
        location_list.append(location)        
    index +=1
###Top row###
index = 0
while index < len(letter_list):
    letter = letter_list[index]
    if int(location_list[index]) == 2:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[2][1] = letter
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 3:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][2] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[1][2] = letter
        index +=1
    elif int(location_list[index]) == 4:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][3] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[1][3] = letter
        index +=1
    elif int(location_list[index]) == 5:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[2][4] = letter             
        else:
            fulltable[1][3] = letter
        index +=1
    ###Side column###
    elif int(location_list[index]) == 7:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[1][2] = letter             
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 13:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][1] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[2][1] = letter
        index +=1
    elif int(location_list[index]) == 19:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][1] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[3][1] = letter
        index +=1
    elif int(location_list[index]) == 25:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[4][2] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    ##Bottom Row##
    elif int(location_list[index]) == 32:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[3][1] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    elif int(location_list[index]) == 33:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][2] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[4][2] = letter
        index +=1
    elif int(location_list[index]) == 34:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][3] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[4][3] = letter
        index +=1
    elif int(location_list[index]) == 35:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[3][4] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    ##Side column##
    elif int(location_list[index]) == 30:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[4][3] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    elif int(location_list[index]) == 24:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][4] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[3][4] = letter
        index +=1
    elif int(location_list[index]) == 18:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][4] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[2][4] = letter
        index +=1
    elif int(location_list[index]) == 12:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[1][3] = letter
        else:
            fulltable[1][4] = letter
        index +=1
row1_2 = row2_1[1:5]
row2_2 = row3_1[1:5]
row3_2 = row4_1[1:5]
row4_2 = row5_1[1:5]
newtable = [row1_2, row2_2, row3_2, row4_2]
column1 = [row[0] for row in newtable]
column2 = [row[1] for row in newtable]
column3 = [row[2] for row in newtable]
column4 = [row[3] for row in newtable]
list_columns = [column1, column2, column3, column4]
totalrows = row1_2 + row2_2 + row3_2 + row4_2
count1 = totalrows.count("0")
count1r = row1_2.count("0")
count2r = row2_2.count("0")
count3r = row3_2.count("0")
count4r = row4_2.count("0")
countc1 = column1.count("0")
countc2 = column2.count("0")
countc3 = column3.count("0")
countc4 = column4.count("0")
for i in range(25):
    for row in newtable:
        countr = row.count('0')
        if countr == 1:
            index = row.index('0')
            if 'A' not in row:
                row[index] = 'A'
            elif 'B' not in row:
                row[index] = 'B'
            elif 'C' not in row:
                row[index] = 'C'

    countc1 = column1.count('0')
    if countc1 == 1:
        index1 = column1.index('0')
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'
            
        countc2 = column2.count('0')
        if countc2 == 1:
            index2 = column2.index('0')
            if 'A' not in column2:
                newtable[index2][1] = 'A'
            elif 'B' not in column2:
                newtable[index2][1] = 'B'
            elif 'C' not in column2:
                newtable[index2][1] = 'C'
            elif 'D' not in column2:
                newtable[index2][1] = 'D'
        countc3 = column3.count('0')
        if countc3 == 1:
            index3 = column3.index('0')
            if 'A' not in column3:
                newtable[index3][2] = 'A'
            elif 'B' not in column3:
                newtable[index3][2] = 'B'
            elif 'C' not in column3:
                newtable[index3][2] = 'C'
            elif 'D' not in column3:
                newtable[index3][2] = 'D'
        countc4 = column4.count('0')
        if countc4 == 1:
            index4 = column4.index('0')
            if 'A' not in column4:
                newtable[index4][3] = 'A'
            elif 'B' not in column4:
                newtable[index4][3] = 'B'
            elif 'C' not in column4:
                newtable[index4][3] = 'C'
            elif 'D' not in column4:
                newtable[index4][2] = 'D'
        i+=1


          #####
    countr1 = row1_2.count('0')
    if countr1 == 2:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' in row1_2:
            row1_2[index] = 'B'
        elif 'B' in row1_2 or 'C' in row1_2:
            row1_2[index] = 'A'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr2 = row2_2.count('0')
    if countr2 == 2:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr3 = row3_2.count('0')
    if countr3 == 2:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr4 = row4_2.count('0')
    if countr4 == 2:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]
        #Loop the 1 0 loop again
    for i in range(25):
        for row in newtable:
            countr = row.count('0')
            if countr == 1:
                index = row.index('0')
                if 'A' not in row:
                    row[index] = 'A'
                elif 'B' not in row:
                    row[index] = 'B'
                elif 'C' not in row:
                    row[index] = 'C'

        countc1 = column1.count('0')
        if countc1 == 1:
            index1 = column1.index('0')
            if 'A' not in column1:
                newtable[index1][0] = 'A'
            elif 'B' not in column1:
                newtable[index1][0] = 'B'
            elif 'C' not in column1:
                newtable[index1][0] = 'C'
            elif 'D' not in column1:
                newtable[index1][0] = 'D'
                
            countc2 = column2.count('0')
            if countc2 == 1:
                index2 = column2.index('0')
                if 'A' not in column2:
                    newtable[index2][1] = 'A'
                elif 'B' not in column2:
                    newtable[index2][1] = 'B'
                elif 'C' not in column2:
                    newtable[index2][1] = 'C'
                elif 'D' not in column2:
                    newtable[index2][1] = 'D'
            countc3 = column3.count('0')
            if countc3 == 1:
                index3 = column3.index('0')
                if 'A' not in column3:
                    newtable[index3][2] = 'A'
                elif 'B' not in column3:
                    newtable[index3][2] = 'B'
                elif 'C' not in column3:
                    newtable[index3][2] = 'C'
                elif 'D' not in column3:
                    newtable[index3][2] = 'D'
            countc4 = column4.count('0')
            if countc4 == 1:
                index4 = column4.index('0')
                if 'A' not in column4:
                    newtable[index4][3] = 'A'
                elif 'B' not in column4:
                    newtable[index4][3] = 'B'
                elif 'C' not in column4:
                    newtable[index4][3] = 'C'
                elif 'D' not in column4:
                    newtable[index4][2] = 'D'
            i+=1

    column1 = [row[0] for row in newtable]
    countc1 = column1.count('0')
    if countc1 == 2:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    column2 = [row[1] for row in newtable]
    countc2 = column2.count('0')
    if countc2 == 2:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    column3 = [row[2] for row in newtable]
    countc3 = column3.count('0')
    if countc3 == 2:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    column4 = [row[3] for row in newtable]
    countc4 = column4.count('0')
    if countc4 == 2:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column4 = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    countr1 = row1_2.count('0')
    if countr1 == 3:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' not in row1_2:
            row1_2[index] = 'A'
        elif 'B' not in row1_2:
            row1_2[index] = 'B'
        elif 'C' not in row1_2:
            row1_2[index] = 'C'
        elif 'D' not in row1_2:
            row1_2[index] = 'D'

    countr2 = row2_2.count('0')
    if countr2 == 3:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'

    countr3 = row3_2.count('0')
    if countr3 == 3:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'

    countr4 = row4_2.count('0')
    if countr4 == 3:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'

    countc1 = column1.count('0')
    if countc1 == 3:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    countc2 = column2.count('0')
    if countc2 == 3:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    countc3 = column3.count('0')
    if countc3 == 3:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    countc4 = column4.count('0')
    if countc4 == 3:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    if location1 == 8:
        letter = newtable[0][0]
    elif location1 == 9:
        letter = newtable[0][1]
    elif location1 == 10:
        letter = newtable[0][2]
    elif location1 == 11:
        letter = newtable[0][3]
    elif location1 == 14:
        letter = newtable[1][0]
    elif location1 == 15:
        letter = newtable[1][1]
    elif location1 == 16:
        letter = newtable[1][2]
    elif location1 == 17:
        letter = newtable[1][3]
    elif location1 == 20:
        letter = newtable[2][0]
    elif location1 == 21:
        letter = newtable[2][1]
    elif location1 == 22:
        letter = newtable[2][2]
    elif location1 == 23:
        letter = newtable[2][3]
    elif location1 == 26:
        letter = newtable[3][0]
    elif location1 == 27:
        letter = newtable[3][1]
    elif location1 == 28:
        letter = newtable[3][2]
    elif location1 == 29:
        letter = newtable[3][3]
        
print("3. ", letter)
print()

input4 = input("4. ")

input4_split = input4.split(", ")
row1_1 = ["0", "0", "0", "0", "0", "0"]
row2_1 = ["0", "0", "0", "0", "0", "0"]
row3_1 = ["0", "0", "0", "0", "0", "0"]
row4_1 = ["0", "0", "0", "0", "0", "0"]
row5_1 = ["0", "0", "0", "0", "0", "0"]
row6_1 = ["0", "0", "0", "0", "0", "0"]

assign1 = int(input4_split[0])
assign2 = int(input4_split[1])
assign3 = int(input4_split[2])
assign4 = int(input4_split[3])

fulltable = [row1_1, row2_1, row3_1, row4_1, row5_1, row6_1]
##fill in filler stuff##
def assignfill(assign1):
    placer1 = 0
    placec1 = 0
    if assign1//6 == assign1/6:
        placer1 = (assign1//6)-1
    else:
        placer1 = assign1//6
    placec1 = assign1 % 6
    placec1 = placec1 - 1

    fulltable[placer1][placec1] = 'D'

assignfill(assign1)
assignfill(assign2)
assignfill(assign3)
assignfill(assign4)

input4_split = input4_split[5: len(input4_split)]

location1 = int(input4_split.pop(len(input4_split)-1))


##fill in letters##
index = 0
location_list = []
letter_list = []
while index < len(input4_split):
    if index % 2 == 0:
        letter = input4_split[index]
        letter_list.append(letter)
    else:
        location = input4_split[index]
        location_list.append(location)        
    index +=1
###Top row###
index = 0
while index < len(letter_list):
    letter = letter_list[index]
    if int(location_list[index]) == 2:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[2][1] = letter
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 3:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][2] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[1][2] = letter
        index +=1
    elif int(location_list[index]) == 4:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][3] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[1][3] = letter
        index +=1
    elif int(location_list[index]) == 5:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[2][4] = letter             
        else:
            fulltable[1][3] = letter
        index +=1
    ###Side column###
    elif int(location_list[index]) == 7:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[1][2] = letter             
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 13:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][1] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[2][1] = letter
        index +=1
    elif int(location_list[index]) == 19:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][1] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[3][1] = letter
        index +=1
    elif int(location_list[index]) == 25:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[4][2] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    ##Bottom Row##
    elif int(location_list[index]) == 32:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[3][1] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    elif int(location_list[index]) == 33:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][2] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[4][2] = letter
        index +=1
    elif int(location_list[index]) == 34:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][3] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[4][3] = letter
        index +=1
    elif int(location_list[index]) == 35:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[3][4] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    ##Side column##
    elif int(location_list[index]) == 30:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[4][3] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    elif int(location_list[index]) == 24:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][4] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[3][4] = letter
        index +=1
    elif int(location_list[index]) == 18:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][4] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[2][4] = letter
        index +=1
    elif int(location_list[index]) == 12:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[1][3] = letter
        else:
            fulltable[1][4] = letter
        index +=1
row1_2 = row2_1[1:5]
row2_2 = row3_1[1:5]
row3_2 = row4_1[1:5]
row4_2 = row5_1[1:5]
newtable = [row1_2, row2_2, row3_2, row4_2]
column1 = [row[0] for row in newtable]
column2 = [row[1] for row in newtable]
column3 = [row[2] for row in newtable]
column4 = [row[3] for row in newtable]
list_columns = [column1, column2, column3, column4]
totalrows = row1_2 + row2_2 + row3_2 + row4_2
count1 = totalrows.count("0")
count1r = row1_2.count("0")
count2r = row2_2.count("0")
count3r = row3_2.count("0")
count4r = row4_2.count("0")
countc1 = column1.count("0")
countc2 = column2.count("0")
countc3 = column3.count("0")
countc4 = column4.count("0")
for i in range(25):
    for row in newtable:
        countr = row.count('0')
        if countr == 1:
            index = row.index('0')
            if 'A' not in row:
                row[index] = 'A'
            elif 'B' not in row:
                row[index] = 'B'
            elif 'C' not in row:
                row[index] = 'C'

    countc1 = column1.count('0')
    if countc1 == 1:
        index1 = column1.index('0')
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'
            
        countc2 = column2.count('0')
        if countc2 == 1:
            index2 = column2.index('0')
            if 'A' not in column2:
                newtable[index2][1] = 'A'
            elif 'B' not in column2:
                newtable[index2][1] = 'B'
            elif 'C' not in column2:
                newtable[index2][1] = 'C'
            elif 'D' not in column2:
                newtable[index2][1] = 'D'
        countc3 = column3.count('0')
        if countc3 == 1:
            index3 = column3.index('0')
            if 'A' not in column3:
                newtable[index3][2] = 'A'
            elif 'B' not in column3:
                newtable[index3][2] = 'B'
            elif 'C' not in column3:
                newtable[index3][2] = 'C'
            elif 'D' not in column3:
                newtable[index3][2] = 'D'
        countc4 = column4.count('0')
        if countc4 == 1:
            index4 = column4.index('0')
            if 'A' not in column4:
                newtable[index4][3] = 'A'
            elif 'B' not in column4:
                newtable[index4][3] = 'B'
            elif 'C' not in column4:
                newtable[index4][3] = 'C'
            elif 'D' not in column4:
                newtable[index4][2] = 'D'
        i+=1


          #####
    countr1 = row1_2.count('0')
    if countr1 == 2:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' in row1_2:
            row1_2[index] = 'B'
        elif 'B' in row1_2 or 'C' in row1_2:
            row1_2[index] = 'A'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr2 = row2_2.count('0')
    if countr2 == 2:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr3 = row3_2.count('0')
    if countr3 == 2:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr4 = row4_2.count('0')
    if countr4 == 2:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]
        #Loop the 1 0 loop again
    for i in range(25):
        for row in newtable:
            countr = row.count('0')
            if countr == 1:
                index = row.index('0')
                if 'A' not in row:
                    row[index] = 'A'
                elif 'B' not in row:
                    row[index] = 'B'
                elif 'C' not in row:
                    row[index] = 'C'

        countc1 = column1.count('0')
        if countc1 == 1:
            index1 = column1.index('0')
            if 'A' not in column1:
                newtable[index1][0] = 'A'
            elif 'B' not in column1:
                newtable[index1][0] = 'B'
            elif 'C' not in column1:
                newtable[index1][0] = 'C'
            elif 'D' not in column1:
                newtable[index1][0] = 'D'
                
            countc2 = column2.count('0')
            if countc2 == 1:
                index2 = column2.index('0')
                if 'A' not in column2:
                    newtable[index2][1] = 'A'
                elif 'B' not in column2:
                    newtable[index2][1] = 'B'
                elif 'C' not in column2:
                    newtable[index2][1] = 'C'
                elif 'D' not in column2:
                    newtable[index2][1] = 'D'
            countc3 = column3.count('0')
            if countc3 == 1:
                index3 = column3.index('0')
                if 'A' not in column3:
                    newtable[index3][2] = 'A'
                elif 'B' not in column3:
                    newtable[index3][2] = 'B'
                elif 'C' not in column3:
                    newtable[index3][2] = 'C'
                elif 'D' not in column3:
                    newtable[index3][2] = 'D'
            countc4 = column4.count('0')
            if countc4 == 1:
                index4 = column4.index('0')
                if 'A' not in column4:
                    newtable[index4][3] = 'A'
                elif 'B' not in column4:
                    newtable[index4][3] = 'B'
                elif 'C' not in column4:
                    newtable[index4][3] = 'C'
                elif 'D' not in column4:
                    newtable[index4][2] = 'D'
            i+=1

    column1 = [row[0] for row in newtable]
    countc1 = column1.count('0')
    if countc1 == 2:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    column2 = [row[1] for row in newtable]
    countc2 = column2.count('0')
    if countc2 == 2:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    column3 = [row[2] for row in newtable]
    countc3 = column3.count('0')
    if countc3 == 2:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    column4 = [row[3] for row in newtable]
    countc4 = column4.count('0')
    if countc4 == 2:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column4 = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    countr1 = row1_2.count('0')
    if countr1 == 3:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' not in row1_2:
            row1_2[index] = 'A'
        elif 'B' not in row1_2:
            row1_2[index] = 'B'
        elif 'C' not in row1_2:
            row1_2[index] = 'C'
        elif 'D' not in row1_2:
            row1_2[index] = 'D'

    countr2 = row2_2.count('0')
    if countr2 == 3:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'

    countr3 = row3_2.count('0')
    if countr3 == 3:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'

    countr4 = row4_2.count('0')
    if countr4 == 3:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'

    countc1 = column1.count('0')
    if countc1 == 3:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    countc2 = column2.count('0')
    if countc2 == 3:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    countc3 = column3.count('0')
    if countc3 == 3:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    countc4 = column4.count('0')
    if countc4 == 3:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    if location1 == 8:
        letter = newtable[0][0]
    elif location1 == 9:
        letter = newtable[0][1]
    elif location1 == 10:
        letter = newtable[0][2]
    elif location1 == 11:
        letter = newtable[0][3]
    elif location1 == 14:
        letter = newtable[1][0]
    elif location1 == 15:
        letter = newtable[1][1]
    elif location1 == 16:
        letter = newtable[1][2]
    elif location1 == 17:
        letter = newtable[1][3]
    elif location1 == 20:
        letter = newtable[2][0]
    elif location1 == 21:
        letter = newtable[2][1]
    elif location1 == 22:
        letter = newtable[2][2]
    elif location1 == 23:
        letter = newtable[2][3]
    elif location1 == 26:
        letter = newtable[3][0]
    elif location1 == 27:
        letter = newtable[3][1]
    elif location1 == 28:
        letter = newtable[3][2]
    elif location1 == 29:
        letter = newtable[3][3]

print("4. ", letter)
print()

input5 = input("5. ")

input5_split = input5.split(", ")
#####################################################################
row1_1 = ["0", "0", "0", "0", "0", "0"]
row2_1 = ["0", "0", "0", "0", "0", "0"]
row3_1 = ["0", "0", "0", "0", "0", "0"]
row4_1 = ["0", "0", "0", "0", "0", "0"]
row5_1 = ["0", "0", "0", "0", "0", "0"]
row6_1 = ["0", "0", "0", "0", "0", "0"]

assign1 = int(input5_split[0])
assign2 = int(input5_split[1])
assign3 = int(input5_split[2])
assign4 = int(input5_split[3])

fulltable = [row1_1, row2_1, row3_1, row4_1, row5_1, row6_1]
##fill in filler stuff##
def assignfill(assign1):
    placer1 = 0
    placec1 = 0
    if assign1//6 == assign1/6:
        placer1 = (assign1//6)-1
    else:
        placer1 = assign1//6
    placec1 = assign1 % 6
    placec1 = placec1 - 1

    fulltable[placer1][placec1] = 'D'

assignfill(assign1)
assignfill(assign2)
assignfill(assign3)
assignfill(assign4)

input5_split = input5_split[5: len(input5_split)]

location1 = int(input5_split.pop(len(input5_split)-1))


##fill in letters##
index = 0
location_list = []
letter_list = []
while index < len(input5_split):
    if index % 2 == 0:
        letter = input5_split[index]
        letter_list.append(letter)
    else:
        location = input5_split[index]
        location_list.append(location)        
    index +=1
###Top row###
index = 0
while index < len(letter_list):
    letter = letter_list[index]
    if int(location_list[index]) == 2:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[2][1] = letter
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 3:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][2] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[1][2] = letter
        index +=1
    elif int(location_list[index]) == 4:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][3] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[1][3] = letter
        index +=1
    elif int(location_list[index]) == 5:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[2][4] = letter             
        else:
            fulltable[1][3] = letter
        index +=1
    ###Side column###
    elif int(location_list[index]) == 7:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][1] != "0":
            fulltable[1][2] = letter             
        else:
            fulltable[1][1] = letter
        index +=1
    elif int(location_list[index]) == 13:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][1] != "0":
            fulltable[2][2] = letter
        else:
            fulltable[2][1] = letter
        index +=1
    elif int(location_list[index]) == 19:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][1] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[3][1] = letter
        index +=1
    elif int(location_list[index]) == 25:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[4][2] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    ##Bottom Row##
    elif int(location_list[index]) == 32:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][1] != "0":
            fulltable[3][1] = letter
        else:
            fulltable[4][1] = letter
        index +=1
    elif int(location_list[index]) == 33:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][2] != "0":
            fulltable[3][2] = letter
        else:
            fulltable[4][2] = letter
        index +=1
    elif int(location_list[index]) == 34:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][3] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[4][3] = letter
        index +=1
    elif int(location_list[index]) == 35:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[3][4] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    ##Side column##
    elif int(location_list[index]) == 30:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[4][4] != "0":
            fulltable[4][3] = letter
        else:
            fulltable[4][4] = letter
        index +=1
    elif int(location_list[index]) == 24:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[3][4] != "0":
            fulltable[3][3] = letter
        else:
            fulltable[3][4] = letter
        index +=1
    elif int(location_list[index]) == 18:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[2][4] != "0":
            fulltable[2][3] = letter
        else:
            fulltable[2][4] = letter
        index +=1
    elif int(location_list[index]) == 12:
        placer1 = 0
        placec1 = 0
        placer1 = int(location_list[index])//6
        placec1 = int(location_list[index]) % 6
        if fulltable[1][4] != "0":
            fulltable[1][3] = letter
        else:
            fulltable[1][4] = letter
        index +=1
row1_2 = row2_1[1:5]
row2_2 = row3_1[1:5]
row3_2 = row4_1[1:5]
row4_2 = row5_1[1:5]
newtable = [row1_2, row2_2, row3_2, row4_2]
column1 = [row[0] for row in newtable]
column2 = [row[1] for row in newtable]
column3 = [row[2] for row in newtable]
column4 = [row[3] for row in newtable]
list_columns = [column1, column2, column3, column4]
totalrows = row1_2 + row2_2 + row3_2 + row4_2
count1 = totalrows.count("0")
count1r = row1_2.count("0")
count2r = row2_2.count("0")
count3r = row3_2.count("0")
count4r = row4_2.count("0")
countc1 = column1.count("0")
countc2 = column2.count("0")
countc3 = column3.count("0")
countc4 = column4.count("0")
for i in range(25):
    for row in newtable:
        countr = row.count('0')
        if countr == 1:
            index = row.index('0')
            if 'A' not in row:
                row[index] = 'A'
            elif 'B' not in row:
                row[index] = 'B'
            elif 'C' not in row:
                row[index] = 'C'

    countc1 = column1.count('0')
    if countc1 == 1:
        index1 = column1.index('0')
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'
            
        countc2 = column2.count('0')
        if countc2 == 1:
            index2 = column2.index('0')
            if 'A' not in column2:
                newtable[index2][1] = 'A'
            elif 'B' not in column2:
                newtable[index2][1] = 'B'
            elif 'C' not in column2:
                newtable[index2][1] = 'C'
            elif 'D' not in column2:
                newtable[index2][1] = 'D'
        countc3 = column3.count('0')
        if countc3 == 1:
            index3 = column3.index('0')
            if 'A' not in column3:
                newtable[index3][2] = 'A'
            elif 'B' not in column3:
                newtable[index3][2] = 'B'
            elif 'C' not in column3:
                newtable[index3][2] = 'C'
            elif 'D' not in column3:
                newtable[index3][2] = 'D'
        countc4 = column4.count('0')
        if countc4 == 1:
            index4 = column4.index('0')
            if 'A' not in column4:
                newtable[index4][3] = 'A'
            elif 'B' not in column4:
                newtable[index4][3] = 'B'
            elif 'C' not in column4:
                newtable[index4][3] = 'C'
            elif 'D' not in column4:
                newtable[index4][2] = 'D'
        i+=1


          #####
    countr1 = row1_2.count('0')
    if countr1 == 2:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' in row1_2:
            row1_2[index] = 'B'
        elif 'B' in row1_2 or 'C' in row1_2:
            row1_2[index] = 'A'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr2 = row2_2.count('0')
    if countr2 == 2:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr3 = row3_2.count('0')
    if countr3 == 2:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]

    countr4 = row4_2.count('0')
    if countr4 == 2:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'
        newtable = [row1_2, row2_2, row3_2, row4_2]
        #Loop the 1 0 loop again
    for i in range(25):
        for row in newtable:
            countr = row.count('0')
            if countr == 1:
                index = row.index('0')
                if 'A' not in row:
                    row[index] = 'A'
                elif 'B' not in row:
                    row[index] = 'B'
                elif 'C' not in row:
                    row[index] = 'C'

        countc1 = column1.count('0')
        if countc1 == 1:
            index1 = column1.index('0')
            if 'A' not in column1:
                newtable[index1][0] = 'A'
            elif 'B' not in column1:
                newtable[index1][0] = 'B'
            elif 'C' not in column1:
                newtable[index1][0] = 'C'
            elif 'D' not in column1:
                newtable[index1][0] = 'D'
                
            countc2 = column2.count('0')
            if countc2 == 1:
                index2 = column2.index('0')
                if 'A' not in column2:
                    newtable[index2][1] = 'A'
                elif 'B' not in column2:
                    newtable[index2][1] = 'B'
                elif 'C' not in column2:
                    newtable[index2][1] = 'C'
                elif 'D' not in column2:
                    newtable[index2][1] = 'D'
            countc3 = column3.count('0')
            if countc3 == 1:
                index3 = column3.index('0')
                if 'A' not in column3:
                    newtable[index3][2] = 'A'
                elif 'B' not in column3:
                    newtable[index3][2] = 'B'
                elif 'C' not in column3:
                    newtable[index3][2] = 'C'
                elif 'D' not in column3:
                    newtable[index3][2] = 'D'
            countc4 = column4.count('0')
            if countc4 == 1:
                index4 = column4.index('0')
                if 'A' not in column4:
                    newtable[index4][3] = 'A'
                elif 'B' not in column4:
                    newtable[index4][3] = 'B'
                elif 'C' not in column4:
                    newtable[index4][3] = 'C'
                elif 'D' not in column4:
                    newtable[index4][2] = 'D'
            i+=1

    column1 = [row[0] for row in newtable]
    countc1 = column1.count('0')
    if countc1 == 2:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    column2 = [row[1] for row in newtable]
    countc2 = column2.count('0')
    if countc2 == 2:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    column3 = [row[2] for row in newtable]
    countc3 = column3.count('0')
    if countc3 == 2:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    column4 = [row[3] for row in newtable]
    countc4 = column4.count('0')
    if countc4 == 2:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column4 = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    countr1 = row1_2.count('0')
    if countr1 == 3:
        row1_2 = "".join(row1_2)
        index = row1_2.find('0')
        row1_2 = list(row1_2)
        if 'A' not in row1_2:
            row1_2[index] = 'A'
        elif 'B' not in row1_2:
            row1_2[index] = 'B'
        elif 'C' not in row1_2:
            row1_2[index] = 'C'
        elif 'D' not in row1_2:
            row1_2[index] = 'D'

    countr2 = row2_2.count('0')
    if countr2 == 3:
        row2_2 = "".join(row2_2)
        index = row2_2.find('0')
        row2_2 = list(row2_2)
        if 'A' not in row2_2:
            row2_2[index] = 'A'
        elif 'B' not in row2_2:
            row2_2[index] = 'B'
        elif 'C' not in row2_2:
            row2_2[index] = 'C'
        elif 'D' not in row2_2:
            row2_2[index] = 'D'

    countr3 = row3_2.count('0')
    if countr3 == 3:
        row3_2 = "".join(row3_2)
        index = row3_2.find('0')
        row3_2 = list(row3_2)
        if 'A' not in row3_2:
            row3_2[index] = 'A'
        elif 'B' not in row3_2:
            row3_2[index] = 'B'
        elif 'C' not in row3_2:
            row3_2[index] = 'C'
        elif 'D' not in row3_2:
            row3_2[index] = 'D'

    countr4 = row4_2.count('0')
    if countr4 == 3:
        row4_2 = "".join(row4_2)
        index = row4_2.find('0')
        row4_2 = list(row4_2)
        if 'A' not in row4_2:
            row4_2[index] = 'A'
        elif 'B' not in row4_2:
            row4_2[index] = 'B'
        elif 'C' not in row4_2:
            row4_2[index] = 'C'
        elif 'D' not in row4_2:
            row4_2[index] = 'D'

    countc1 = column1.count('0')
    if countc1 == 3:
        column1 = "".join(column1)
        index1 = column1.find('0')
        column1 = list(column1)
        if 'A' not in column1:
            newtable[index1][0] = 'A'
        elif 'B' not in column1:
            newtable[index1][0] = 'B'
        elif 'C' not in column1:
            newtable[index1][0] = 'C'
        elif 'D' not in column1:
            newtable[index1][0] = 'D'

    countc2 = column2.count('0')
    if countc2 == 3:
        column2 = "".join(column2)
        index2 = column2.find('0')
        column2 = list(column2)
        if 'A' not in column2:
            newtable[index2][1] = 'A'
        elif 'B' not in column2:
            newtable[index2][1] = 'B'
        elif 'C' not in column2:
            newtable[index2][1] = 'C'
        elif 'D' not in column2:
            newtable[index2][1] = 'D'

    countc3 = column3.count('0')
    if countc3 == 3:
        column3 = "".join(column3)
        index3 = column3.find('0')
        column3 = list(column3)
        if 'A' not in column3:
            newtable[index3][2] = 'A'
        elif 'B' not in column3:
            newtable[index3][2] = 'B'
        elif 'C' not in column3:
            newtable[index3][2] = 'C'
        elif 'D' not in column3:
            newtable[index3][2] = 'D'

    countc4 = column4.count('0')
    if countc4 == 3:
        column4 = "".join(column4)
        index4 = column4.find('0')
        column = list(column4)
        if 'A' not in column4:
            newtable[index4][3] = 'A'
        elif 'B' not in column4:
            newtable[index4][3] = 'B'
        elif 'C' not in column4:
            newtable[index4][3] = 'C'
        elif 'D' not in column4:
            newtable[index4][2] = 'D'

    if location1 == 8:
        letter = newtable[0][0]
    elif location1 == 9:
        letter = newtable[0][1]
    elif location1 == 10:
        letter = newtable[0][2]
    elif location1 == 11:
        letter = newtable[0][3]
    elif location1 == 14:
        letter = newtable[1][0]
    elif location1 == 15:
        letter = newtable[1][1]
    elif location1 == 16:
        letter = newtable[1][2]
    elif location1 == 17:
        letter = newtable[1][3]
    elif location1 == 20:
        letter = newtable[2][0]
    elif location1 == 21:
        letter = newtable[2][1]
    elif location1 == 22:
        letter = newtable[2][2]
    elif location1 == 23:
        letter = newtable[2][3]
    elif location1 == 26:
        letter = newtable[3][0]
    elif location1 == 27:
        letter = newtable[3][1]
    elif location1 == 28:
        letter = newtable[3][2]
    elif location1 == 29:
        letter = newtable[3][3]

print("5. ", letter)

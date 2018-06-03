"""
Takoma Park M.S.
Jr-5
Contest 3
Shreeya Khurana
"""
print("""Please input your values separated by COMMAS WITH SPACES AFTER
For example, the first input could be 3, 1, A, 3, C, 8, A
""")
input1 = input("1. ")
input2 = input("2. ")
input3 = input("3. ")
input4 = input("4. ")
input5 = input("5. ")

input1_split = input1.split(", ")
input2_split = input2.split(", ")
input3_split = input3.split(", ")
input4_split = input4.split(", ")
input5_split = input5.split(", ")

input1_split.pop(0)
input2_split.pop(0)
input3_split.pop(0)
input4_split.pop(0)
input5_split.pop(0)


####For Input 1####
index = 0
location_list = []
letter_list = []
while index < len(input1_split):
    if index % 2 == 0:
        location = input1_split[index]
        location_list.append(location)
    else:
        letter = input1_split[index]
        letter_list.append(letter)
    index +=1
list_grids = ["ABCBCACAB", "ABCCABBCA", "ACBBACCBA", "ACBCBABAC", "BACACBCBA", "BACCBAACB", "BCAABCCAB", "BCACABABC", "CABABCBCA", "CABBCAABC", "CBAACBBAC", "CBABACACB"]
found = False
index = 0
while found == False:
    good = True
    for blank in location_list:
        item = int(blank) - 1
        prove = list_grids[index]
        if prove[item] != letter_list[location_list.index(blank)]:
            good = False
    if good == True:
        found = True
        answer1 = prove
    else:
        index = index + 1
print("1. ", answer1)

####For Input 2####
index = 0
location_list = []
letter_list = []
while index < len(input2_split):
    if index % 2 == 0:
        location = input2_split[index]
        location_list.append(location)
    else:
        letter = input2_split[index]
        letter_list.append(letter)
    index +=1
list_grids = ["ABCBCACAB", "ABCCABBCA", "ACBBACCBA", "ACBCBABAC", "BACACBCBA", "BACCBAACB", "BCAABCCAB", "BCACABABC", "CABABCBCA", "CABBCAABC", "CBAACBBAC", "CBABACACB"]
found = False
index = 0
while found == False:
    good = True
    for blank in location_list:
        item = int(blank) - 1
        prove = list_grids[index]
        if prove[item] != letter_list[location_list.index(blank)]:
            good = False
    if good == True:
        found = True
        answer2 = prove
    else:
        index = index + 1
print("2. ", answer2)
####For Input 3####
index = 0
location_list = []
letter_list = []
while index < len(input3_split):
    if index % 2 == 0:
        location = input3_split[index]
        location_list.append(location)
    else:
        letter = input3_split[index]
        letter_list.append(letter)
    index +=1
list_grids = ["ABCBCACAB", "ABCCABBCA", "ACBBACCBA", "ACBCBABAC", "BACACBCBA", "BACCBAACB", "BCAABCCAB", "BCACABABC", "CABABCBCA", "CABBCAABC", "CBAACBBAC", "CBABACACB"]
found = False
index = 0
while found == False:
    good = True
    for blank in location_list:
        item = int(blank) - 1
        prove = list_grids[index]
        if prove[item] != letter_list[location_list.index(blank)]:
            good = False
    if good == True:
        found = True
        answer3 = prove
    else:
        index = index + 1
print("3. ", answer3)
####For Input 4####
index = 0
location_list = []
letter_list = []
while index < len(input4_split):
    if index % 2 == 0:
        location = input4_split[index]
        location_list.append(location)
    else:
        letter = input4_split[index]
        letter_list.append(letter)
    index +=1
list_grids = ["ABCBCACAB", "ABCCABBCA", "ACBBACCBA", "ACBCBABAC", "BACACBCBA", "BACCBAACB", "BCAABCCAB", "BCACABABC", "CABABCBCA", "CABBCAABC", "CBAACBBAC", "CBABACACB"]
found = False
index = 0
while found == False:
    good = True
    for blank in location_list:
        item = int(blank) - 1
        prove = list_grids[index]
        if prove[item] != letter_list[location_list.index(blank)]:
            good = False
    if good == True:
        found = True
        answer4 = prove
    else:
        index = index + 1
print("4. ", answer4)
####For Input 5####
index = 0
location_list = []
letter_list = []
while index < len(input5_split):
    if index % 2 == 0:
        location = input5_split[index]
        location_list.append(location)
    else:
        letter = input5_split[index]
        letter_list.append(letter)
    index +=1
list_grids = ["ABCBCACAB", "ABCCABBCA", "ACBBACCBA", "ACBCBABAC", "BACACBCBA", "BACCBAACB", "BCAABCCAB", "BCACABABC", "CABABCBCA", "CABBCAABC", "CBAACBBAC", "CBABACACB"]
found = False
index = 0
while found == False:
    good = True
    for blank in location_list:
        item = int(blank) - 1
        prove = list_grids[index]
        if prove[item] != letter_list[location_list.index(blank)]:
            good = False
    if good == True:
        found = True
        answer5 = prove
    else:
        index = index + 1
print("5. ", answer5)        

####Outputs####
print()
print()
print()
print("FINAL OUTPUTS")
print("1. ", answer1)
print("2. ", answer2)
print("3. ", answer3)
print("4. ", answer4)
print("5. ", answer5)


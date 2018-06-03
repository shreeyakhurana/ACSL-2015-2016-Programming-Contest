"""
Takoma Park M.S.
Jr-5
Contest 2
Shreeya Khurana
"""
print("Jr-5 2015-16 Contest2")
print("First input the desired string")
print("Then input the start value and the length value separated by commas ")
print("Ex. 0,2 for a start value of 0 and a length value of 2")
print("(SEPARATE BY COMMA, WITH A SPACE AFTER EACH COMMA)")
print("""Press Enter to move to next input line (there will be 5 total
after the first string input)""")
print()
print()
string = str(input("1. "))
INDEX1 = input("2. ")
INDEX2 = input("3. ")
INDEX3 = input("4. ")
INDEX4 = input("5. ")
INDEX5 = input("6. ")
print()
print()
print()


Index1_list = INDEX1.split(', ')
Index2_list = INDEX2.split(', ')
Index3_list = INDEX3.split(', ')
Index4_list = INDEX4.split(', ')
Index5_list = INDEX5.split(', ')

start1 = Index1_list[0]
length1 = Index1_list[1]
start1_int = int(start1)
length1_int = int(length1)

start2 = Index2_list[0]
length2 = Index2_list[1]
start2_int = int(start2)
length2_int = int(length2)

start3 = Index3_list[0]
length3 = Index3_list[1]
start3_int = int(start3)
length3_int = int(length3)

start4 = Index4_list[0]
length4 = Index4_list[1]
start4_int = int(start4)
length4_int = int(length4)

start5 = Index5_list[0]
length5 = Index5_list[1]
start5_int = int(start5)
length5_int = int(length5)
#Output1
if start1_int >= 0 and length1_int == 0:
    output1 = string[start1_int:len(string)]
elif start1_int >=0 and length1_int > 0:
    output1 = string[start1_int:(start1_int + length1_int)]
elif start1_int >=0 and length1_int < 0:
    output1 = string[start1_int:length1_int]
elif start1_int < 0 and length1_int == 0:
    output1 = string[start1_int:len(string)]
elif start1_int < 0 and length1_int > 0:
    output1 = string[start1_int:(start1_int + length1_int)]
elif start1_int < 0 and length1_int < 0:
    output1 = string[start1_int:length1_int]
print("1.", output1)
#Output2
if start2_int >= 0 and length2_int == 0:
    output2 = string[start2_int:len(string)]
elif start2_int >=0 and length2_int > 0:
    output2 = string[start2_int:(start2_int + length2_int)]
elif start2_int >=0 and length2_int < 0:
    output2 = string[start2_int:length2_int]
elif start2_int < 0 and length2_int == 0:
    output2 = string[start2_int:len(string)]
elif start2_int < 0 and length2_int > 0:
    output2 = string[start2_int:(start2_int + length2_int)]
elif start2_int < 0 and length2_int < 0:
    output2 = string[start2_int:length2_int]
print("2.", output2)
#Ouput3
if start3_int >= 0 and length3_int == 0:
    output3 = string[start3_int:len(string)]
elif start3_int >=0 and length3_int > 0:
    output3 = string[start3_int:(start3_int + length3_int)]
elif start3_int >=0 and length3_int < 0:
    output3 = string[start3_int:length3_int]
elif start3_int < 0 and length3_int == 0:
    output3 = string[start3_int:len(string)]
elif start3_int < 0 and length3_int > 0:
    output3 = string[start1_int:(start3_int + length3_int)]
elif start3_int < 0 and length3_int < 0:
    output3 = string[start3_int:length3_int]
print("3.", output3)
#Output4
if start4_int >= 0 and length4_int == 0:
    output4 = string[start4_int:len(string)]
elif start4_int >=0 and length4_int > 0:
    output4 = string[start4_int:(start4_int + length4_int)]
elif start4_int >=0 and length4_int < 0:
    output4 = string[start4_int:length4_int]
elif start4_int < 0 and length4_int == 0:
    output4 = string[start4_int:len(string)]
elif start4_int < 0 and length4_int > 0:
    output4 = string[start4_int:(start4_int + length4_int)]
elif start4_int < 0 and length4_int < 0:
    output4 = string[start4_int:length4_int]
print("4.", output4)
#Output5
if start5_int >= 0 and length5_int == 0:
    output5 = string[start5_int:len(string)]
elif start5_int >=0 and length5_int > 0:
    output5 = string[start5_int:(start5_int + length5_int)]
elif start5_int >=0 and length5_int < 0:
    output5 = string[start5_int:length5_int]
elif start5_int < 0 and length5_int == 0:
    output5 = string[start5_int:len(string)]
elif start5_int < 0 and length5_int > 0:
    output5 = string[start5_int:(start5_int + length5_int)]
elif start5_int < 0 and length5_int < 0:
    output5 = string[start5_int:length5_int]
print("5.", output5)

#Final Outputs
print()
print()
print()
print("FINAL OUTPUTS OF SUBSTRINGS")
print("1.", output1)
print("2.", output2)
print("3.", output3)
print("4.", output4)
print("5.", output5)

input("Please press enter to close program.")

    

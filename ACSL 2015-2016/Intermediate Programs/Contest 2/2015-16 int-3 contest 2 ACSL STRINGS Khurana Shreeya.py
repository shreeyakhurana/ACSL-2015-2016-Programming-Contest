"""
Takoma Park M.S
Int-3
Contest 2
Shreeya Khurana
"""
print("Int-3 2015-16 Contest 2")
print(""" Input the character string (a$)and the
data for the arguments needed in the following functions:
char_split(a$,n,'char') --> Hello,2,* 
strrem(a$,b$) --> Hello,lo
strchr(a$,b$) --> Hello,H
strtok(a$,b$) --> Hello,e
wordwrap(a$,n,b$) --> Hello,2,l
(SEPARATE BY COMMA(S), WITH A SPACE AFTER EACH COMMA) 
Please press enter after each input (there will be 5 total)
""")

INPUT1 = input("1. ")
INPUT2 = input("2. ")
INPUT3 = input("3. ")
INPUT4 = input("4. ")
INPUT5 = input("5. ")
print()
print()
print()

Input1_split = INPUT1.split(', ')
Input2_split = INPUT2.split(', ')
Input3_split = INPUT3.split(', ')
Input4_split = INPUT4.split(', ')
Input5_split = INPUT5.split(', ')


#Char_split
if len(Input1_split)== 2:
    astring1 = str(Input1_split[0])
    number1 = int(Input1_split[1])
    char1 = Input1_split[2]
    
#strrem
if len(Input2_split)== 1:
    astring2 = str(Input2_split[0])
    bstring2 = str(Input2_split[1])
    
#strchr    
if len(Input3_split)== 1:
    astring3 = str(Input3_split[0])
    bstring3 = str(Input3_split[1])
    
#strtok   
if len(Input4_split)== 1:
    astring4 = str(Input4_split[0])
    bstring4 = str(Input4_split[1])
 
#wordwrap   
if len(Input5_split)== 2:
    astring5 = str(Input5_split[0])
    number5 = int(Input5_split[1])
    bstring5 = str(Input5_split[2])

#Evaluating char_split
import textwrap
astring1 = str(Input1_split[0])
number1 = int(Input1_split[1])
astring1_split = textwrap.wrap(astring1, number1)

char1 = str(Input1_split[2])
astring1_final = char1.join(astring1_split)
print("1. ",astring1_final)

#Evaluating strrem
astring2 = str(Input2_split[0])
bstring2 = str(Input2_split[1])

astring2_final = astring2.replace(bstring2,'')
print("2. ",astring2_final)
#Evaluating strchr
astring3 = str(Input3_split[0])
bstring3 = str(Input3_split[1])

index3 = astring3.find(bstring3)
astring3_final = astring3[0:int(index3)]
print("3. ",astring3_final)
#Evaluating strtok
astring4 = str(Input4_split[0])
bstring4 = str(Input4_split[1])

astring4_split = astring4.split(bstring4)
astring4_strtok = [astring4_split[0]] + [bstring4+l for l in astring4_split[1:]]


astring4_final = " ".join(astring4_strtok)
print("4. ",astring4_final)

#Evaluating wordwrap
astring5 = str(Input5_split[0])
number5 = int(Input5_split[1])
bstring5 = str(Input5_split[2])

global final_split
final_split = ""
global firstindex
firstindex = 0
while len(astring5) > 0:
    if bstring5 in astring5:
        index1 = astring5.find(bstring5)
    else:
        index1 = 0
    firstindex = 0
    var1  = astring5[0:abs(index1-firstindex)]
    if len(var1)  > (number5):
        var1 = astring5[0:abs(number5-firstindex)]
        length = len(var1)
        final_split = final_split.strip()
        final_split = final_split +" " +var1
        firstindex = abs(length)
        astring5 = astring5[firstindex: len(astring5)]

        
    else:
        if index1 == 0:
            var1 = astring5[index1:number5]
            length = len(var1)
            final_split = final_split.strip()
            final_split = final_split +" "+var1
            firstindex = length
            astring5 = astring5[firstindex: len(astring5)]

            
        else:
            var1  = astring5[0:abs(index1-firstindex)]
            length = len(var1)
            final_split = final_split.strip()
            final_split = final_split + " "+var1
            firstindex = length
            astring5 = astring5[firstindex: len(astring5)]

            
final_split = final_split.strip()
print("5. ",final_split)
        


###FINAL OUTPUTS
print()
print()
print()
print()
print("FINAL OUTPUTS")
print("1.", astring1_final)
print("2.", astring2_final)
print("3.", astring3_final)
print("4.", astring4_final)
print("5.", final_split)


input("Please press enter to close the program.")









        
    

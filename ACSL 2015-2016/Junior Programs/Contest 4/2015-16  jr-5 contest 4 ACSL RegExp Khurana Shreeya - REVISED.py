"""
Takoma Park M.S.
Jr-5
Contest 4
Shreeya Khurana
"""

print(""" On line 1, enter a list of ten character strings separated by commas
and a space and use the pound sign (#) to represent an empty string,for example
(abc, ac, a, abbc, acc, abcc, abb, aaaab, abbba, #).
On lines 2 through 6, enter the regular expressions to be tested.
The outputs will be printed all at the same time. The empty string in the output
will be represented by a pound sign (#)
""")

charstrlist = input("1. ")
input1 = input("2. ")
input2 = input("3. ")
input3 = input("4. ")
input4 = input("5. ")
input5 = input("6. ")
print()

if input1 == '':
    input1 = '#'
if input2 == '':
    input2 = '#'
if input3 == '':
    input3 = '#'
if input4 == '':
    input4 = '#'
if input5 == '':
    input5 = '#'



import re
def regexp(charstrlist, inputs):
    if '#' in charstrlist:
        charstrlist = charstrlist.replace('#', ' ')
    charstrlist = charstrlist.split(', ')
    answerlist = []
    for strings in charstrlist:
        answers = re.match("(?:" + inputs + r")\Z", strings)
        #answers = re.fullmatch(inputs, strings)
        if answers:  #If answer exists
            answerlist.append(strings) #this string works
        else:
            answerlist.append('NONE')
        if len(answerlist) > 0:      
            if 'NONE' in answerlist:     
                answerlist.remove('NONE') 
    if len(inputs) == 4 and inputs.count('?') == 2:
        if ' ' in charstrlist:
            answerlist.append('#')
    elif len(inputs) == 4 and inputs.count('*') == 1 and inputs.count('?') == 1:
        if ' ' in charstrlist:
            answerlist.append('#')
    elif len(inputs) == 4 and inputs.count('*') == 2:
        if ' ' in charstrlist:
            answerlist.append('#')
    elif len(inputs) == 2 and '?' in inputs:
        if ' ' in charstrlist:
            answerlist.append('#')
    elif len(inputs) == 2 and '*' in inputs:
        if ' ' in charstrlist:
            answerlist.append('#')
    if len(answerlist) == 0:
        output = "NONE"
    else:        
        output = ', '.join(answerlist)      
    print(output)

print("OUTPUTS")
print()
print("1. ")
regexp(charstrlist, input1)
print()
print("2. ")
regexp(charstrlist, input2)
print()
print("3. ")
regexp(charstrlist, input3)
print()
print("4. ")
regexp(charstrlist, input4)
print()
print("5. ")
regexp(charstrlist, input5)


  

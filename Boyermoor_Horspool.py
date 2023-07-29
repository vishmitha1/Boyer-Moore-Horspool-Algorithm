p="pattern1.txt"
with open(p,'r') as file:
    pattern1=file.read()
t="text1.txt"
with open(t,'r') as file:
    text=file.read()

file=open('output.txt','w')
table={}

def rightmost(pattern, character):
    return pattern.rfind(character)
        


def HpBc(pattern):
    temp=len(pattern)-1
    for x in pattern:
        if(x!= pattern[temp]):
            if rightmost(pattern,x)-1>0:
                table[x]=rightmost(pattern,x)-1
            else:
                table[x]=0   

def CheckPaternMatch(possition,text,pattern):
    substring = text[possition:possition+len(pattern)]
    if(substring==pattern):
        return True
    else:
        return False
        

#HpBc(pattern1)    
#print(table)
# Next shift possition = position + table[text[possition+length-1]]

def Boyermoore(text,pattern):
    possition=0
    matchings=True
    HpBc(pattern)
    while(possition<len(text)-len(pattern)):
        if (CheckPaternMatch(possition,text,pattern)==True):
            #print("Pattern found at index :" , possition)
            file.write("Pattern found at index  : %d \n" % possition)
            matchings +1
        if text[possition+len(pattern)-1] in table:
            possition = possition + table[text[possition+len(pattern)-1]]
          
        else:
            possition = possition + len(pattern)
        
        if(matchings==0):
            print("Pattern not found in given text ")


Boyermoore(text,pattern1)
file.close()
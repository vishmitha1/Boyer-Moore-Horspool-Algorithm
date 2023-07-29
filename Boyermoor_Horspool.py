pattern1="xtpxtd"
text="xluxtpxtdqwtpxtpxtsyxtpxtdy"
#print(len(pattern))
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
    HpBc(pattern)
    while(possition<len(text)-len(pattern)):
        if (CheckPaternMatch(possition,text,pattern)==True):
            print("Pattern found at index :" , possition)
           
        if text[possition+len(pattern)-1] in table:
            possition = possition + table[text[possition+len(pattern)-1]]
          
        else:
            possition = possition + len(pattern)
           
    
Boyermoore(text,pattern1)
print(table)
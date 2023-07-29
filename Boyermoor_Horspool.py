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
# Next shift possition = position + table[text[possition]+length-1]
possition=0
def Boyermoore(text,pattern):
    HpBc(pattern)
    while(possition<len(text)-len(pattern1)):
        if (CheckPaternMatch(possition,text,pattern)):
            print("Pattern found at index :" , possition)
        possition = possition + table[text[possition]+len(text)-1]

Boyermoore(text,pattern1)
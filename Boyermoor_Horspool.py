pattern1="abcd"
text="aabcdnbabcd"
#print(len(pattern))
table={}

def rightmost(pattern, character):
    return pattern.rfind(character)
        


def HpBc(pattern):
    temp=len(pattern)-1
    for x in pattern:
        if(x!= pattern[temp]):
            table[x]=rightmost(pattern,x)-1

HpBc(pattern1)    
print(table)
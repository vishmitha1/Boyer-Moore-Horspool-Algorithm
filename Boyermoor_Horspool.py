pattern1="abcbd"
text="aabcdnbabcd"
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

HpBc(pattern1)    
print(table)
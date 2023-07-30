p="pattern1.txt"                                    #read patern file
with open(p,'r') as file:
    pattern1=file.read()
t="text1.txt"
with open(t,'r') as file:                           #read text file
    text=file.read()
print(text[3])
file=open('output.txt','w')                         #open outputfile
table={}

def rightmost(pattern, character):                  #this finction helps to find rightmost characters indx
    return pattern.rfind(character)
        

def HpBc(pattern):                                  #This function helps to Create HpBc Table
    temp=len(pattern)-1
    for x in pattern:
        if(x!= pattern[temp]):
            if rightmost(pattern,x)-1>0:
                table[x]=len(pattern)-rightmost(pattern,x)-1
            else:
                table[x]=0   

def CheckPaternMatch(possition,text,pattern):        #this Function use for to checking pattern matching
    substring = text[possition:possition+len(pattern)]
   
    if(substring==pattern):
        return True
    else:
        return False
        
# Next shift possition = position + table[text[possition+length-1]]

def Boyermoore(text,pattern):                       # in this function calling all other sub functions                      
    possition=0
    matchings=0
    HpBc(pattern)
    while(possition<len(text)-len(pattern)):
        if (CheckPaternMatch(possition,text,pattern)==True):
            print("Pattern found at index :" , possition)
            file.write("Pattern found at index  : %d \n" % possition)
            matchings=matchings+1
        if text[possition+len(pattern)-1] in table:
            possition = possition + table[text[possition+len(pattern)-1]]
          
        else:
            possition = possition + len(pattern)
        
    if(matchings==0):
            print("Pattern not found in given text ")
            file.write("Pattern not found in given text ")    


Boyermoore(text,pattern1)
file.close()


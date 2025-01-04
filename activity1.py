#take input of a word
string = input("pleasse enter your own word")
print(len(string))
#take input of a character
char = input("please enter your own charcter : ")
i=0
count=0
#loop will to find the occurence of charcter 
while(i<len(string)): #string opertation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i+1

#display the result
print("the total number of times ", char, " has occured = " , count)
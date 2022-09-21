#simple while

a=3
while(a<6):
    print(a,end="\t")
    a=a+1
print("\n")


#while with else

a=2
while(a<1):
    print(a,end="  ")#this way we can give space between each value of a
else:
    print(a," is greater than 1, so else part of while is executed")



"""
Variations of for loop
Check everyformat by seeing its results
"""

print("\n\n")


#type1
for i in range(3):
    print (i)
print("\n")

#type2
for i in range(0,3):
    print (i)
print("\n")

#type3
for i in range(8,0,-2):
    print (i)
print("\n")


#iterating through string 
for eachCharacter in "Akhil":
    print(eachCharacter)
print("\n")


#iterating through array
"""will see array,tuple,dictionary and list in another chapter
for now just know that the next line holds an array of size 4"""
array1=[10,11,12,13]
for eachElementInArray in array1:
    print(eachElementInArray)
print("\n")



#Python does not have built in 
        #do_while or switch
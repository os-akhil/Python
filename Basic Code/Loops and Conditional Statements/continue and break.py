#continue will skip all the next step and will get out of the loop  around it without processing
#all the next steps

print("Example of break:")
for i in range(5):
    if(i==3):
        break
    print(i)
#this break will exit from for loop


#continue will skip the steps that matches a condition
#steps that does not meet the condition will continue to run 

print("Example of continue:")
for i in range(5):
    if(i==3):
        continue
    print(i)
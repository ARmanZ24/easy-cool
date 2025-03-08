#Give: In a given list of positive numbers, find the missing number in within the range (between the min and max in the list) 
usrList = list(map(int,input("Enter your list of positive non-zero numbers: ").split()))
usrList.sort() #sorting the user given list using built-in fn
missingNum=1 #initialize it as int

if all((num>0 for num in usrList)): #Stays true only if all values in the list are > 0
    for i in range(0,len(usrList)-1):
        if(usrList[i+1]-usrList[i] == 1): #condition check to find the if the next number is missing in the sorted order
            continue
        else:
            missingNum = usrList[i]+1
    print("The only missing number in the given list is: ", missingNum)

else:
    print("Invalid value found in the list")


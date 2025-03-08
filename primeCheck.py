#Given: Check the given number is prime number or not

counter=-1 #counter to flag any changes while checking
userIp=1 #initializing the user value as integer

while userIp != -2: #infinte loop to accept the input from the user until the break value is received
    userIp = int(input("Enter a non-zero positive number to check if it's a prime number (Enter -2 to end the program): "))
    if(userIp == -2): #checks for break value
        break
    elif userIp <=0: # checks for invalid value. Prime number should be greater than 1
        print("Invalid input!. Try again..")
    else:
        for i in range(2,int(userIp/2)+1): #for loop to determine the status of the value
            if(userIp%i == 0):
                counter+=1
            else:
                continue

        if(counter == -1):  #executes if it's a prime number
            print("It's a Prime Number")
            counter=-1
        else:               #executes if it's NOT a prime number
            print("No, it's not a Prime Number")
            counter=-1

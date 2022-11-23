#Author - Jayspray
#Team - Dillusioners
#Word - Settlers
#Info - Helping people settle legally in the mysterious country called Deblands

#Importing necessary packages
import random
import os
import json

#Just a display function for users
def display():
    print("Welcome to the Debland ,the best country ever\nRegister as a citizen to settle in the country !!")
    print("Would you like to : \n1.Create a citizen card\n2.Check your details\n3.Delete Card\nOr any other number to exit")

#Function to check data of a citizen 
def citz_check():
    #try-except block to handle errors
    try:
        #getting the code of citizen
        code = int(input("Enter your transaction id : "))
        fna = 'H:\AdvancedJava\PythonCode\Other\Cards'+'\\'+str(code)
        #Opening file with code as name and printing data
        with open(fna,'r')as x:
            data = x.read()
            print("Your information is: ",data)
        #Catching errors
    except Exception as e:
        print("OOps something went wrong :(\nError is -> ",e)

#Delete() to delete ids
def delete():
    #Again try-except
    try:
        #Getting code
        code = int(input("Enter your transaction id : "))
        fna = 'H:\AdvancedJava\PythonCode\Other\Cards'+'\\'+str(code)
        #Checking if code exists
        if os.path.exists(fna):
            #if yes we remove the file
            os.remove(fna)
            print("Thank you for being a part of Deblands, we wish you goodluck on your new journey.")
        else:
            print("You are not a citizen")
            exit()
    except Exception as e:
        print("OOps something went wrong :(\nError is -> ",e)
    
#Function to create citizen card
def data_inp():
    try:
        #Basic inputs and loggers
        f_name = input("Enter your first name : ")
        l_name = input("Enter your last name : ")
        while True:
            age = int(input("Enter your age : "))
            if age < 0 or age > 120:
                print("Please enter valid age")
            else:
                break
        country = (input("Which country did you belong to previously : "))
        while True:
            ph = int(input("Enter your valid phone number : "))
            if ph > 999999999 or ph < 100000000:
                print("Please enter valid phone number")
            else:
                break
        t_code = random.randint(1000,9999)
    except Exception as e:
        print("OOPs something went wrong\Error is ->",e)
    else:
        print("Your citizen code is :",t_code)
        #Gathering data
        data = {
                "fname":f_name,
                "lname":l_name,
                "age":age,
                "country":country,
                "phone":ph,
                "transaction":t_code
               }
        #Dumping json data in file created
        filename = 'H:\AdvancedJava\PythonCode\Other\Cards'+'\\'+str(t_code)
        jsonObj = json.dumps(data)
        with open(filename,"w") as f:
            f.write(jsonObj)

        print("Thank your for being a citizen at Deblands\n You are now authorised here to settle")

#Main function to work based upon choices
def main():
    display()
    choice = int(input())
    if choice != 1 and choice != 2 and choice != 3:
        print("Bye Bye")
    elif choice == 1:
        data_inp()
    elif choice == 3:
        delete()
    else:
        citz_check()
#Execute() to invoke the main method and create the necessary directories
def execute():
    try:
        if not os.path.exists('Cards'):
            os.makedirs('Cards')
            main()
        else:
            main()
    except Exception as e:
        print("Error: " + str(e))
#Calling execute()
execute()

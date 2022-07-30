#Log in account creation

from tkinter import END, N, Y


print("Create an Account")
firstname=str(input("Enter your First Name : "))
Lastname=str(input("Enter your Last Name : "))
Username=input("Enter your Username : ")
gender=str(input('Gender : '))
phone=int(input('Enter your phone number : '))
password=input("Enter your password : ")

print("Your account has been sucessfully created")
print("log in now")

log_user =input("Enter your Username : ")
log_pass =input("Enter your Password : ")

t1 = password
t2 = password

if log_user == Username and log_pass == password:
    print("Log in sucessful...")
    
else:
    print("Incorect credentials..")
    print("Try again...")
    t1=input("Re-enter your password : ")
if t1 == password:
    print('Log in sucessful..')
else:
    print('''
          incorrect password
          last atempt ...''')
    t2=input("Re-enter your password : ")
if t2 == password:
    print("Log in sucessful...")
else:
    print("Account Locked")
    print("Do you want to recover account ? ")
    yes = Y
    no = N
    option=input("""
    > press  Y for Yes
    > press N for No
    >""")
    if option is Y:
        print("Recover account...")
        rec_acc = input("Enter your username : ")
        rec_phone = input("Enter your phone number : ")
        new_pass = input("Enter a new password : ")
        confirm_pass = input("Confirm your password : ")
    
    if confirm_pass == new_pass:
            str(print(firstname + Lastname + " your password has been sucessfully changed"))
    else:
            print("YOUR ACCOUNT HAS BEEN BLOCKED BY JONATHAN ") 
   
        


    

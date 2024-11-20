password = "Python is awesome"
while True:
    entered_password = input("Enter password: ")
    if entered_password == password:
        print("ACCESS GRANTED")
        break 
    else:
        print("ACCESS DENIED")

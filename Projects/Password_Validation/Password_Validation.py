print(" Password requirements- \n 1) Your password MUST be between 8 and 16 characters in length.\n 2) Your password MUST have at least one UPPERCASE character.\n 3) Your password MUST have at least one LOWERCASE character.\n 4) Your password MUST have at least one number.\n 5) Your password MUST have at least one Special (Non-Alphanumeric) character (eg. ! @ # $ % ^ & * ).\n 6) Your password MUST NOT contain spaces./n 7) Your password MUST NOT contain part of your name or username.")
Password=input("Enter your password: ")
Name = input("Enter your name: ")
letter = list(filter(lambda c: c.isupper(), Password))
letter2 = list(filter(lambda b:b.islower(),Password))
digit = list(filter(lambda a:a.isdigit(),Password))
space = list(filter(lambda d:d.isspace(),Password))
if len(Password)<8 ^ len(Password)>16:
    if letter:
        print("Error 2")
    elif not letter2:
        if digit:
            print("Error 4")
        elif ("@" in Password)^("!" in Password)^("#" in Password)^("$" in Password)^("%" in Password)^("^" in Password)^("&" in Password)^("*" in Password):
            if space:
                if Name.lower() in Password:
                    print("Error 7")
            else:
                print ("Error 6")
        else:
            print("Error 5")
    else:
        print("Error 3")
else:
    print("Error 1")
    
    
   #By-Arindam Majumder

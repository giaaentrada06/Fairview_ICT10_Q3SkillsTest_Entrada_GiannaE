def check_account(username, password):

    if len(username) < 7:
        print("Username too short")

    if len(password) < 10:
        print("Password too short")

    # basic check for letter
    has_letter = False
    for c in password:
        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            has_letter = True

    if has_letter == True:
        print("Password needs a letter")
    has_letter = False
    
    for c in username:
        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            has_letter = True

    if has_letter == True:
        print("Password needs a letter")
    
    
    # basic check for number
    has_number = False
    for c in password:
        if c >= '0' and c <= '9':
            has_number = True

    if has_number == False:
        print("Password needs a number")

    if len(username) >= 7 and len(password) >= 10 and has_letter and has_number:
        print("Account OK")



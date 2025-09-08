user_email = input("Enter your email: ")
space, upper_char, other_symbols = 0, 0, 0
if len(user_email) >= 6:
    if user_email[0].isalpha():
        if ('@' in user_email) and (user_email.count('@') == 1):
            if (user_email[-3] == '.') or (user_email[-4] == '.'):
                for i in user_email:
                    if i == i.isspace():
                        space = 1
                    elif i.isalpha():
                        if i == i.upper():
                            upper_char = 1
                    elif i.isdigit():
                        continue
                    elif i == '.' or i == '_' or i == '@':
                        continue
                    else:
                        other_symbols = 1
                if space == 1 or upper_char == 1 or other_symbols == 1:
                    print("Invalid Email")
                else:
                    print("Valid Email..")
            else:
                print("Invalid Email (dot error)")
        else:
            print("Invlaid Email (at sign error)")
    else:
        print("Invalid Email (First digit error)")
else:
    print("Invalid Email (length error)")
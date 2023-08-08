print("Welcome to the Health Management System.\n")


def getdate():
    import datetime
    return datetime.datetime.now


while True:
    choice1 = int(input("Enter 1 to log or 2 to retrieve:\n"))
    if choice1 not in [1, 2]:
        print("Please enter correct option.\n")
        continue
    else:
        if choice1 == 1:
            while True:
                choice2 = int(input("Enter 1 for ved, 2 for saksham  and 3 for yash:\n"))
                if choice2 not in [1, 2, 3]:
                    print("Please enter correct option.\n")
                    continue
                else:
                    if choice2 in [1, 2, 3]:
                        while True:
                            choice3 = int(input("Enter 1 for exercise, 2 for diet:\n"))
                            if choice3 not in [1, 2]:
                                print("Please enter correct option.\n")
                                continue
                            else:
                                if choice3 == 1:
                                    exercise = input("Enter what exercise you have done:\n")
                                    str1 = "[" + str(getdate()) + "] " + exercise + "\n"
                                    if choice2 == 1:
                                        with open("ved_f.txt", "a") as f:
                                            f.write(str1)
                                        break
                                    if choice2 == 2:
                                        with open("saksham_f.txt", "a") as f:
                                            f.write(str1)
                                        break
                                    if choice2 == 3:
                                        with open("yash_f.txt", "a") as f:
                                            f.write(str1)
                                        break
                                else:
                                    diet = input("Enter your current food intake:\n")
                                    str2 = "[" + str(getdate()) + "] " + diet + "\n"
                                    if choice2 == 1:
                                        with open("ved_e.txt", "a") as f:
                                            f.write(str2)
                                        break
                                    if choice2 == 2:
                                        with open("saksham_e.txt", "a") as f:
                                            f.write(str2)
                                        break
                                    if choice2 == 3:
                                        with open("yash_e.txt", "a") as f:
                                            f.write(str2)
                                        break
                print("Logged Successfully.")
                break
        else:
            while True:
                choice4 = int(input("Enter 1 for ved log, 2 for saksham log, 3 for yash log:\n"))
                if choice4 not in [1, 2, 3]:
                    print("Please enter a valid option.")
                    continue
                else:
                    while True:
                        choice5 = int(input("Enter 1 for exercise log, 2 for diet log:\n"))
                        if choice5 not in [1, 2]:
                            print("Please enter a valid option.")
                            continue
                        else:
                            if choice5 == 1 and choice4 == 1:
                                with open("ved.txt") as f:
                                    print(f.read())
                            elif choice5 == 1 and choice4 == 2:
                                with open("saksham.txt") as f:
                                    print(f.read())
                            elif choice5 == 1 and choice4 == 3:
                                with open("ved.txt") as f:
                                    print(f.read())
                            elif choice5 == 2 and choice4 == 1:
                                with open("ved_e.txt") as f:
                                    print(f.read())
                            elif choice5 == 2 and choice4 == 2:
                                with open("saksham_e.txt") as f:
                                    print(f.read())
                            else:
                                with open("yash_e.txt") as f:
                                    print(f.read())
                            break
                print("Retrieved successfully.")
                break

    break
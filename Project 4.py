def main():
    try:  
        userNum = int(input("Please enter a number: "))
        if userNum > 50:
            print(userNum, "is greater then 50!")
        elif userNum == 50:
            print(userNum, "is equal to 50")
        elif userNum < 50:
            print(userNum, "is less than 50!")
        else:
            main()
    except (ValueError, TabError) as error:
            print("Sorry, you did not enter a number.")
                ## Asking user to play again      
    try:
        userStr = str(input("Would you like to play again? "))
        if userStr == "yes":
            main()
        elif userStr == "no":
            print("Thank you for playing")  
        elif userStr != "yes" or "no":
            print("Invalid syntax")
    except KeyboardInterrupt:
            print("Sorry, you press the wrong buttons")
        ##User satisfaction
    try:
        userSatis = int(input("Please rate this on a scale from 1-5: "))
        if userSatis == 4 or userSatis == 5:
            print("Glad to hear you enojoyed.")
        elif userSatis < 4 or userSatis < 5:
            print("We are sorry you did not enjoy.")
    except Exception as error:
        error_string = str(error)
        print("Sorry, you did not enter a number3.")
        quit()
main()


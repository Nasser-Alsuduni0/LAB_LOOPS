for number in range(45 , 210):
    if number == 100 :
        continue
    elif number == 205 :
        break
    print(number)


while True:
    user_answer = float(input("what is the product of 7 * 24 ? \n"))
    if user_answer == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")

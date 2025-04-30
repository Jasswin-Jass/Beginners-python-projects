import random

def number_choosing():
    num = random.randint(1,100)
    return num

def guessing(easyhard,num):

    for i in range(easyhard):
        print(f"You have {easyhard} attempts remaining")
        guess_no = int(input("Enter you guess:"))

        if guess_no == num :
            print(f"{num} is the correct number, You win!")
            return
        else:

            if guess_no > num :
                print("Too high")

            else:
                print("Too low")

            easyhard -= 1
            continue
    else:
        print("You lose!")


print("Wellcome to the guessing game")
easyorhard = input("Enter whether you want it to be 'easy' or 'hard':").lower()
chosen_number = number_choosing()

if easyorhard == "easy":
    guessing(10, chosen_number)

elif easyorhard == "hard":
    guessing(5, chosen_number)

else:
    print("invalid choice")
    
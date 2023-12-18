import random
def initialize():
    while True:
        user_chances = int(input("how many chances do you want? "))
        if 50 >= user_chances >= 3:
            print('Great! you have', user_chances, 'chances to guess.')
            break
        else:
            print('your chances must be between the range of 3 to 50, try again')
    print("your requested range gap must not be less than 50")
    while True:
        start_number = int(input('what is the start number?: '))
        end_number = int(input('what is the end number?: '))
        subtract = abs(start_number - end_number)
        if subtract >= 50:
            print("thank you! now the game starts! let's have some fun!! ")
            break
        else:
            print('the gap less than 50 is not valid.')
    the_number = random.randrange(start=start_number, stop=end_number)
    user_chances1 = user_chances
    while user_chances1 > 0:
        guess1 = int(input('guess the number!: '))
        if guess1 == the_number:
            print("Bravo! That's right!")
            break
        elif guess1 > the_number:
            user_chances -= 1
            print('Nope! Try again. You have', user_chances, 'chance(s) left')
            print('the number is less than ', guess1)
        elif guess1 < the_number:
            user_chances -= 1
            print('Nope! Try again. You have', user_chances, 'chance(s) left')
            print('the number is greater than', guess1)
        if user_chances == 0:
                print('Sorry, your chances reached the limit!')
                break

user_name = input('what is your name? ')
name = user_name
print('hello', name)

initialize()

while True:
    start_over = int(input('Do you want to play again? if yes, type 0 if not type 1: '))
    if start_over == 0:
        initialize()
    else:
        print('had a nice time with you! I hope you come back soon!  bye.')
        break









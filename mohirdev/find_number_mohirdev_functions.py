import random
from pprint import pprint


def find_number():
    numbers = list(range(1, 11))
    random_number = random.choice(numbers)
    print('Can you find a number within 1to 10')
    user_counts = 0
    while True:
        answer = int(input('Your number: '))
        user_counts += 1
        if answer > random_number:
            print('Incorrect my number is lower than your number')
        elif answer < random_number:
            print('Incorrect my number is higher than your number')
        elif answer == random_number:
              print(f'Correct you found {user_counts} times')
              break
    print(f'Now it is  your turn think number and i will try to find it')
    return user_counts

def find_number_pc():

    numbers = list(range(1, 11))
    low = 0
    high = len(numbers) - 1
    pc_counts=0
    for i in range(len(numbers)):
        pc_counts += 1
        mid_number = (low + high) // 2

        user_answer2 = input(f'I found is it {numbers[mid_number]} yes or no ').lower()
        if user_answer2 == 'yes':
            print('I knew it')
            break
        elif user_answer2 == 'no':
            user_answer3 = input('Is your number higher or lower ').lower()
            if user_answer3 == 'higher':
                low = mid_number + 1
            else:
                high = mid_number - 1
    return pc_counts

def lets_play():
    play_again = True
    while play_again:
        user_trials=find_number()
        pc_trials=find_number_pc()
        if user_trials > pc_trials:
            print("I won you're looser")
        elif user_trials < pc_trials:
            print('Oh you have won congratulations Boss')
        else:
            print("oh it's a draw")
        play_again = input('Would you like to play again?y/no').lower()

lets_play()
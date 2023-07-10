import random;import time
def play():
    s = "**\033[31mGuess the Number\033[0m**"
    print(s.center(45))
    name=input('May I know your name: ')
    print(f'Okay! {name}, welcome to Guess the Number.\n')
    time.sleep(3)
    print('I\'m thinking about a number between 1 to 100')
    time.sleep(6)
    choose = random.randint(1,100)
    print('Yup, done.')
    time.sleep(1)
    print('Can you guess it in 7 tries? Don\'t worry there are hints!\nIf yes, what is your guess?: (int input only)')
    for i in range(7):
        guess = int(input())
        if guess in range(choose-5,choose+6) and guess!=choose:
            print('You are VERRYYY close....')
        elif guess in range(choose-10,choose+11) and guess!=choose:
            print('You are very close....')
        elif guess==choose:
            print(f'Your guess is Correct! after {i+1} tries.')
            break
        else:
          if guess>choose:
            print('Guess is far & higher......')
          if guess<choose:
            print('Guess is too far & lower.......')
        if i==6 and guess!=choose:
                print('Your 7 tries is completed!')
    time.sleep(3)
    print(f'The number I choosen is {choose}.')
    time.sleep(1)
    x=input('\nDo you want to play again? ')
    if x[0].lower()=='y':
        print('\033[2J\033[1;1H')
        play()
    else:
        print('\033[2J\033[1;1H')
        print('Thankyou 4 PlayinG')
play()

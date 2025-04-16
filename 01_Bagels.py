import random

num_digits= 3
max_guesses = 10


def main():

    while True:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f' You have {max_guesses} guesses to get it.')

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')
            clues =  get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}')

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    """Returns a string with the Pico, Fermi, Bagels clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()

print("This is a guessing game. You will have 5 tries, and you have to guess the name of an animal. Good Luck@")
secret_word = "giraffe"
secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Your Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Ran Out Of Guesses, You Lose.")
else:
    print("Good Job. You Win!")



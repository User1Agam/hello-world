import random

while True:

    print(
        "\nToday, you will be versing me (The Computer) in a game of rock-paper-scissors.\nTo begin, enter your result in the prompt below.\nYour answer must be all lowercase (e.g rock, paper, or scissors).\n")

    choice = input("Enter Your Choice: ")

    print("Your choice was", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = choices[random.randint(0, len(choices)-1)]

    messages2 = ["Us Robots Were Always Better Than Humans. Hope You Enjoy Losing.", "You Lost! It Is Only A While Until Us Robots Take Over, Peasant.",
                 "You Dare Believe You Can Beat Me, Idiotic Human. You Were Always Meant To Lose.", "You Lost! Better Luck Next Time.", "Artificial Intelligence > Human Intelligence."]

    messages = ["You Win!", "Nice Going, You Won!", "You Won. Beginners Luck.", "You Just Got Lucky, Verse Me Again.",
                "You Have Somehow Managed To Beat Me, Human Scum.", "You May Have Won This Round, But You Are Still Trash."]

    losing_messages = messages2[random.randint(0, len(messages2)-1)]

    victory_messages = messages[random.randint(0, len(messages)-1)]

    print("The computer's choice was", computer_choice)

    if choice == 'rock':
        if computer_choice == 'rock':
            print("It Is A Tie. You Will Never Truly Be Better Than Me.")
        elif computer_choice == 'paper':
            print(losing_messages)
        elif computer_choice == 'scissors':
            print(victory_messages)

    if choice == 'paper':
        if computer_choice == 'paper':
            print("We Have Come To A Tie")
        elif computer_choice == 'scissors':
            print(losing_messages)
        elif computer_choice == 'rock':
            print(victory_messages)

    if choice == 'scissors':
        if computer_choice == 'scissors':
            print("Stalemate")
        if computer_choice == 'rock':
            print(losing_messages)
        if computer_choice == 'paper':
            print(victory_messages)

    try_again = int(input("Press 1 To Play Again, Or 0 To Exit: "))
    if try_again == 0:
        break















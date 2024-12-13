# Rock, Paper, scissors with the computer

import random
# define the required functions

options = ["rock", "paper", "scissors"] # using global variables

def take_Choice():
    user_Choice = input("Enter the option you want (rock, paper, scissors): ").lower()
    # valid check
    while user_Choice not in options:
        print("Invalid option! Please enter a valid one!")
        user_Choice = input("Enter the option you want (rock, paper, scissors): ").lower()
    return user_Choice

def comp_Choice():
    # random
    return random.choice(options)

def declare_Win(user, computer):
    if user == computer:
        return "Its a tie!"
    elif (user=="rock" and computer=="scissors") or \
        (user=="paper" and computer=="rock") or \
        (user=="scissors" and computer=="paper"):
        return "You won!! YAY!"
    else:
        return "Computer won and you lost!"

def main():
    print("Welcome to Rock, Paper, Scissors")
    while True:
        user_input = take_Choice()
        comp_input = comp_Choice()

        print(f"Your chose: ", user_input)
        print(f"\nThe computer chose: ", comp_input)
        output = declare_Win(user_input, comp_input)
        print(output)

        play_Loop = input("Do you want to continue? (yes/no)").lower()
        if play_Loop == "no":
            break
        
    print("Thank you for playing!")

if __name__ == "__main__":
    main()

print("Project ran with 0 errors")

# Q. Try to take the input from the computer as the input from another user
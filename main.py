def playgame():
    import random

    choices = {"rock": 0, "paper": 1, "scissors": 2}
    result_matrix = [
        [0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]
    ]

    def get_user_choice():
        user_input = input("Enter rock, paper or scissors: ").lower()
        while user_input not in choices:
            user_input = input("Invalid! Enter rock, paper or scissors: ").lower()
        return choices[user_input], user_input

    def get_computer_choice():
        comp_input = random.choice(list(choices.keys()))
        return choices[comp_input], comp_input

    def play():
        print("🎮 Rock-Paper-Scissors Game 🎮")
        while True:
            user_index, user_choice = get_user_choice()
            comp_index, comp_choice = get_computer_choice()

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {comp_choice}")

            result = result_matrix[user_index][comp_index]

            if result == 0:
                print("Result: It's a tie!")
            elif result == 1:
               print("Result: You win! 🎉")
            else:
                print("Result: Computer wins! 💻")

            again = input("\nDo you want to play again? (yes/no): ").lower()
            if again != 'yes':
                print("Thanks for playing!")
                break
    play()

if __name__ == "__main__":
    playgame()
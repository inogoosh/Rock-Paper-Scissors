# Rock-Paper-Scissors 🎮
A simple Python command game where you play Rock, Paper, Scissors against the computer. It uses a matrix to determine the winner and loops until you choose to stop.

# 🔐 Secret Message Encoder & Decoder (Python)
This is a simple Python project that lets you encode and decode secret messages using a randomly generated password. It's perfect for beginners who are learning about strings, loops, and basic encryption in Python.

# 🧠 How It Works
- You will be asked to type either **rock**, **paper**, or **scissors**.
- The computer randomly picks one of the three choices.
- A result matrix is used to decide the winner:
  - Rock beats Scissors
  - Paper beats Rock
  - Scissors beats Paper
- If both pick the same, it's a tie.
- After each round, you're asked if you want to play again.

# ✅ Features
- Simple and interactive command-line interface.
- Uses a **determinant matrix** method to decide the winner.
- Keeps asking if you want to replay until you say "no".

# 🚀 How to Run
Make sure you have Python installed.
Download or clone this repo.
Run the Python script

# 🧑‍💻 Code Overview
choices: A dictionary mapping user input to numeric values.

result_matrix: A 3x3 matrix to determine win, lose, or tie.

get_user_choice(): Gets and validates user input.

get_computer_choice(): Randomly picks a choice for the computer.

play(): Handles the game loop and logic.

if __name__ == "__main__": ensures the game runs when the file is executed.

# 💡 Example
🎮 Rock-Paper-Scissors Game 🎮

Enter rock, paper or scissors: rock

You chose: rock

Computer chose: scissors

Result: You win! 🎉

Do you want to play again? (yes/no): no

Thanks for playing!

# 📁 File Structure
📁 SecretMessage/

│

├── main.py (# Main Python script)

├── README.md (# This file)

├── .gitignore

├── LICENSE

# 📚 Concepts Used
1. Functions
2. Dictionaries
3. Lists
4. Random Module
5. Conditional Statements
6. Loops
7. String Methods

*Feel free to use, share, or improve this project!

👨‍💻 Made by Abdullah Umer

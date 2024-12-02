import random
import tkinter as tk
from tkinter import messagebox


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f8ff")  # Light blue background

        self.word = ""
        self.word_completion = ""
        self.guessed_letters = []
        self.tries = 6

        # Title Label
        self.title_label = tk.Label(
            root, text="Hangman Game", font=("Helvetica", 30, "bold"), bg="#f0f8ff", fg="#000000"
        )
        self.title_label.pack(pady=20)

        # Hangman Display
        self.hangman_label = tk.Label(
            root, text=self.display_hangman(), font=("Courier", 20), bg="#f0f8ff", fg="#000000", justify=tk.LEFT
        )
        self.hangman_label.pack(pady=10)

        # Word Display
        self.word_label = tk.Label(
            root, text="", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#000000"
        )
        self.word_label.pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f8ff")
        input_frame.pack(pady=10)

        self.input_label = tk.Label(
            input_frame, text="Enter your guess:", font=("Helvetica", 14), bg="#f0f8ff"
        )
        self.input_label.grid(row=0, column=0, padx=10)

        self.guess_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=10)
        self.guess_entry.grid(row=0, column=1, padx=10)

        self.submit_button = tk.Button(
            input_frame,
            text="Submit",
            font=("Helvetica", 12),
            bg="#000000",
            fg="white",
            activebackground="#006666",
            command=self.submit_guess,
        )
        self.submit_button.grid(row=0, column=2, padx=10)

        # Result Label
        self.result_label = tk.Label(
            root, text="", font=("Helvetica", 16), bg="#f0f8ff", fg="#ff4500"
        )
        self.result_label.pack(pady=10)

        # Reset Button (Initially hidden)
        self.reset_button = tk.Button(
            root,
            text="Play Again",
            font=("Helvetica", 14),
            bg="#4682b4",
            fg="white",
            activebackground="#3a5f8b",
            command=self.reset_game,
        )
        self.reset_button.pack(pady=10)
        self.reset_button.pack_forget()  # Hide initially

        self.reset_game()

    def get_word(self):
        return random.choice(word_list).upper()

    def display_hangman(self):
        stages = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """
]
        
        return stages[self.tries]

    def submit_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) not in {1, len(self.word)}:
            self.result_label.config(text="Invalid input. Enter a letter or the full word.", fg="red")
            return

        if guess in self.guessed_letters:
            self.result_label.config(text=f"You already guessed '{guess}'.", fg="red")
            return

        if len(guess) == 1:
            self.guessed_letters.append(guess)
            if guess in self.word:
                self.result_label.config(text=f"Good job! '{guess}' is in the word.", fg="green")
                self.word_completion = "".join(
                    [letter if letter in self.guessed_letters else "_" for letter in self.word]
                )
            else:
                self.result_label.config(text=f"Wrong guess! '{guess}' is not in the word.", fg="red")
                self.tries -= 1
        elif guess == self.word:
            self.word_completion = self.word
            self.result_label.config(text="You guessed the word! You win!", fg="green")
        else:
            self.result_label.config(text=f"'{guess}' is not the word.", fg="red")
            self.tries -= 1

        self.update_ui()

    def update_ui(self):
        self.hangman_label.config(text=self.display_hangman())
        self.word_label.config(text=" ".join(self.word_completion))

        if "_" not in self.word_completion:
            self.result_label.config(text="Congratulations! You guessed the word!", fg="green")
            self.submit_button.config(state=tk.DISABLED)
            self.reset_button.pack(pady=10)
        elif self.tries == 0:
            self.result_label.config(text=f"Game over! The word was '{self.word}'.", fg="red")
            self.submit_button.config(state=tk.DISABLED)
            self.reset_button.pack(pady=10)

    def reset_game(self):
        self.word = self.get_word()
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.tries = 6

        self.hangman_label.config(text=self.display_hangman())
        self.word_label.config(text=" ".join(self.word_completion))
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.reset_button.pack_forget()


# Word list
word_list = ["PYTHON", "HANGMAN", "DEVELOPER", "CODING", "PROGRAMMING", "ALGORITHM"]

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

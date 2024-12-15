import tkinter as tk
import random
import time

# List of sentences for typing
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests are great for improving keyboard skills.",
    "Python is a versatile programming language.",
    "Consistency is the key to becoming proficient at typing.",
    "Short sentences are easy to type quickly."
]

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.sentence = random.choice(SENTENCES)
        self.start_time = None

        # Instruction label
        self.instruction_label = tk.Label(root, text="Type the sentence below as fast as you can:", font=("Arial", 16))
        self.instruction_label.pack(pady=20)

        # Sentence to type
        self.sentence_label = tk.Label(root, text=self.sentence, font=("Arial", 14), wraplength=600, justify="center")
        self.sentence_label.pack(pady=10)

        # Entry box for typing
        self.text_entry = tk.Entry(root, font=("Arial", 14), width=60)
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<FocusIn>", self.start_timer)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=self.calculate_result)
        self.submit_button.pack(pady=20)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=self.reset_test)
        self.reset_button.pack(pady=10)

    def start_timer(self, event=None):
        if self.start_time is None:  # Start the timer only on the first focus
            self.start_time = time.time()

    def calculate_result(self):
        if self.start_time is None:
            self.result_label.config(text="Start typing to begin the test!")
            return

        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        typed_text = self.text_entry.get().strip()

        if not typed_text:
            self.result_label.config(text="Please type the sentence before submitting!")
            return

        # Calculate WPM
        typed_words = len(typed_text.split())
        wpm = (typed_words / elapsed_time) * 60

        # Check accuracy
        if typed_text == self.sentence:
            self.result_label.config(
                text=f"Great job! Your speed is {wpm:.2f} WPM with 100% accuracy."
            )
        else:
            accuracy = sum(1 for a, b in zip(typed_text, self.sentence) if a == b) / len(self.sentence) * 100
            self.result_label.config(
                text=f"Your speed is {wpm:.2f} WPM with {accuracy:.2f}% accuracy. Keep practicing!"
            )

    def reset_test(self):
        self.start_time = None
        self.sentence = random.choice(SENTENCES)
        self.sentence_label.config(text=self.sentence)
        self.text_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()

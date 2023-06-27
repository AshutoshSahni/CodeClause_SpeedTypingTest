# Project 3 : Typing Speed

import time
import random
import tkinter as tk


class TypingTestApp:
    def __init__(self, master):
        self.master = master
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a versatile programming language.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Learning new things is always exciting.",
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "She sells seashells by the seashore and diligently collects unique shells for her collection.",
            "The orchestra harmoniously synchronizes their instruments, creating a symphony of captivating melodies "
            "and rich harmonies.",
            "The intricacies of quantum physics and the concept of parallel universes baffle even the most brilliant "
            "minds."
        ]
        self.selected_sentence = ""

        self.label = tk.Label(master, text="Press 'Start' to begin the typing test.")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_typing_test)
        self.start_button.pack()

        self.reset_button = tk.Button(master, text="Reset", state=tk.DISABLED, command=self.reset_typing_test)
        self.reset_button.pack()

        self.sentence_label = tk.Label(master, text="")
        self.sentence_label.pack()

        self.results_label = tk.Label(master, text="")
        self.results_label.pack()

        self.accuracy_label = tk.Label(master, text="")
        self.accuracy_label.pack()

        self.entry = None
        self.start_time = 0
        self.end_time = 0

    def start_typing_test(self):
        self.selected_sentence = random.choice(self.sentences)

        self.label.config(text="Type the following text:")
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

        self.sentence_label.config(text=self.selected_sentence)

        self.results_label.config(text="")
        self.accuracy_label.config(text="")

        self.entry = tk.Entry(self.master, width=40)
        self.entry.pack()
        self.entry.focus_set()

        self.entry.bind('<Return>', self.end_typing_test)

        self.start_time = time.time()

    def end_typing_test(self, event):
        self.end_time = time.time()
        self.entry.config(state=tk.DISABLED)

        elapsed_time = self.end_time - self.start_time
        typed_text = self.entry.get()
        words_typed = len(typed_text.split())
        typing_speed = (words_typed / elapsed_time)*60

        self.results_label.config(text=f"Elapsed time: {round(elapsed_time, 2)} seconds\nWords typed: {words_typed}\nTyping speed: {round(typing_speed, 2)} words per minute")

        # Accuracy calculation
        correct_characters = sum([1 for a, b in zip(self.selected_sentence, typed_text) if a == b])
        accuracy = correct_characters / len(self.selected_sentence) * 100
        self.accuracy_label.config(text=f"Accuracy: {round(accuracy, 2)}%")

        self.reset_button.config(state=tk.NORMAL)

    def reset_typing_test(self):
        self.label.config(text="Press 'Start' to begin the typing test.")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

        self.sentence_label.config(text="")
        self.entry.destroy()
        self.entry = None
        self.results_label.config(text="")
        self.accuracy_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Typing Test")
    app = TypingTestApp(root)
    root.mainloop()

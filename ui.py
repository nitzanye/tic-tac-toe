import tkinter as tk
from tkinter import messagebox
from game_logic import on_click, reset_game
import os


def run_game():
    def update_ui(message):
        messagebox.showinfo("Tic-Tac-Toe", message)

    # Suppress deprecation warning
    os.environ['TK_SILENCE_DEPRECATION'] = '1'

    # Create the main window
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("450x650")  # Adjusted to fit larger buttons
    window.resizable(False, False)
    window.configure(bg="#333333")

    # Create a frame to center the buttons
    frame = tk.Frame(window, bg="#333333")
    frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create the buttons for the game board
    buttons = []
    for i in range(9):
        button = tk.Button(frame, text=" ", font=("Helvetica", 24), bg="#ffffff", fg="#333333",
                           relief="groove", activebackground="#e0e0e0", activeforeground="#333333",
                           command=lambda i=i: on_click(i, buttons, update_ui))
        button.grid(row=i // 3, column=i % 3, padx=10, pady=10, ipadx=20, ipady=20)
        buttons.append(button)

    # Add a reset button
    reset_button = tk.Button(window, text="Reset Game", font=("Helvetica", 14), command=lambda: reset_game(buttons),
                             bg="#ff6666", fg="#ffffff", activebackground="#ff4d4d", activeforeground="#ffffff",
                             relief="raised")
    reset_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # Run the main loop
    window.mainloop()

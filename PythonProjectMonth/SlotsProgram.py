# This is the Python code for the slot machine game 
# This will be the main game logic and GUI for the slot machine game.

import tkinter as tk
from tkinter import messagebox
import random

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")

        # Slot Machine Display
        self.slot1 = tk.Label(master, text="?", font=("Helvetica", 48))
        self.slot1.grid(row=0, column=0, padx=10, pady=10)

        self.slot2 = tk.Label(master, text="?", font=("Helvetica", 48))
        self.slot2.grid(row=0, column=1, padx=10, pady=10)

        self.slot3 = tk.Label(master, text="?", font=("Helvetica", 48))
        self.slot3.grid(row=0, column=2, padx=10, pady=10)

        # Spin Lever
        self.spin_lever = tk.Button(master, text="Spin", command=self.spin)
        self.spin_lever.grid(row=1, column=0, columnspan=3, pady=10)

    def spin(self):
        # Generate random numbers for each slot
        self.slot1.config(text=str(random.randint(1, 9)))
        self.slot2.config(text=str(random.randint(1, 9)))
        self.slot3.config(text=str(random.randint(1, 9)))

        # Check for win condition (all slots match)
        if self.slot1.cget("text") == self.slot2.cget("text") == self.slot3.cget("text"):
            messagebox.showinfo("You win!")
        else:
            messagebox.showinfo("Better luck next time!")

    def reset(self):
        self.slot1.config(text="?")
        self.slot2.config(text="?")
        self.slot3.config(text="?")

if __name__ == "__main__":
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()

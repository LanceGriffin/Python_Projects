#!/usr/bin/env python3
"""
Slots Machine Game - GUI Version
Matches the design of SlotsMenu.html and SlotsMenu.css
"""

import tkinter as tk
from tkinter import messagebox
import random

# Color scheme matching the CSS
BG_GRADIENT_1 = "#2c3e50"
BG_GRADIENT_2 = "#4ca1af"
CONTAINER_BG = "#1a1a1a"
TEXT_COLOR = "#f1f1f1"
BUTTON_BG = "#3498db"
BUTTON_HOVER = "#2980b9"
BUTTON_ACTIVE = "#2980b9"

class SlotsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Slots Machine Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Set background to gradient (simulate with a solid dark background)
        self.root.configure(bg=BG_GRADIENT_1)
        
        # Main frame
        self.main_frame = tk.Frame(root, bg=BG_GRADIENT_1)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Centered container frame
        self.container = tk.Frame(
            self.main_frame,
            bg=CONTAINER_BG,
            relief=tk.RAISED,
            bd=2
        )
        self.container.pack(pady=50, padx=20, fill=tk.BOTH, expand=True)
        
        # Title
        self.title_label = tk.Label(
            self.container,
            text="🎰 SLOTS MACHINE 🎰",
            font=("Arial", 28, "bold"),
            bg=CONTAINER_BG,
            fg=TEXT_COLOR
        )
        self.title_label.pack(pady=20)
        
        # Info label
        self.info_label = tk.Label(
            self.container,
            text="Match three symbols to win!",
            font=("Arial", 12),
            bg=CONTAINER_BG,
            fg=TEXT_COLOR
        )
        self.info_label.pack(pady=10)
        
        # Reels frame
        self.reels_frame = tk.Frame(self.container, bg=CONTAINER_BG)
        self.reels_frame.pack(pady=20)
        
        self.reel_labels = []
        self.reels = [None, None, None]  # Current reel values
        
        for i in range(3):
            reel_label = tk.Label(
                self.reels_frame,
                text="?",
                font=("Arial", 40, "bold"),
                bg="#0a0a0a",
                fg="#FFD700",
                width=5,
                relief=tk.SUNKEN,
                bd=2
            )
            reel_label.pack(side=tk.LEFT, padx=10)
            self.reel_labels.append(reel_label)
        
        # Status label
        self.status_label = tk.Label(
            self.container,
            text="Ready to spin!",
            font=("Arial", 12),
            bg=CONTAINER_BG,
            fg=TEXT_COLOR
        )
        self.status_label.pack(pady=15)
        
        # Win counter
        self.wins = 0
        self.counter_label = tk.Label(
            self.container,
            text=f"Wins: {self.wins}",
            font=("Arial", 11),
            bg=CONTAINER_BG,
            fg="#FFD700"
        )
        self.counter_label.pack(pady=5)
        
        # Button frame
        self.button_frame = tk.Frame(self.container, bg=CONTAINER_BG)
        self.button_frame.pack(pady=20)
        
        # Spin button (main action)
        self.spin_btn = self.create_button(
            self.button_frame,
            "SPIN",
            self.spin_reels
        )
        self.spin_btn.pack(pady=8)
        
        # Reset button
        self.reset_btn = self.create_button(
            self.button_frame,
            "Reset",
            self.reset_game
        )
        self.reset_btn.pack(pady=8)
        
        # Quit button
        self.quit_btn = self.create_button(
            self.button_frame,
            "Quit Game",
            self.quit_game
        )
        self.quit_btn.pack(pady=8)
    
    def create_button(self, parent, text, command):
        """Create a styled button matching the CSS"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief=tk.FLAT,
            width=20,
            height=2,
            cursor="hand2",
            bd=0
        )
        
        # Bind hover effects
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_BG))
        
        return btn
    
    def spin_reels(self):
        """Spin the reels and check for wins"""
        symbols = ["🍎", "🍊", "🍋", "🍒", "🍉", "⭐"]
        
        # Simulate reel spin with animation
        self.status_label.config(text="Spinning...", fg="#FFD700")
        self.root.update()
        
        # Determine new reel values
        self.reels = [random.choice(symbols) for _ in range(3)]
        
        # Update display
        for i, reel_label in enumerate(self.reel_labels):
            reel_label.config(text=self.reels[i])
        
        # Check for win
        if self.check_win():
            self.wins += 1
            self.counter_label.config(text=f"Wins: {self.wins}")
            self.status_label.config(text="🎉 YOU WIN! 🎉", fg="#00FF00")
            messagebox.showinfo("WIN!", f"You matched three {self.reels[0]}!\nTotal Wins: {self.wins}")
        else:
            self.status_label.config(text="No match. Try again!", fg=TEXT_COLOR)
    
    def check_win(self):
        """Check if all three reels match"""
        return self.reels[0] == self.reels[1] == self.reels[2]
    
    def reset_game(self):
        """Reset the game"""
        self.wins = 0
        self.reels = [None, None, None]
        self.counter_label.config(text=f"Wins: {self.wins}")
        self.status_label.config(text="Ready to spin!", fg=TEXT_COLOR)
        
        for reel_label in self.reel_labels:
            reel_label.config(text="?")
    
    def quit_game(self):
        """Close the game and return to menu"""
        response = messagebox.askyesno(
            "Quit Game",
            "Are you sure you want to quit?\nYou will return to the menu."
        )
        if response:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = SlotsGame(root)
    root.mainloop()

from Bot import Bot
import tkinter as tk
from tkinter import *


def execute_bot():
    Bot(
        username=username.get(),
        password=password.get(),
        game_name=game_name.get(),
        minutes=int(minutes.get()),
        history_length=int(history_length.get()),
        initial_bet_amount=float(initial_bet_amount.get()),
        loss_multiplicator=int(loss_multiplicator.get()),
        low_threshold=int(low_threshold.get()),
        low_bet_type=low_bet_type.get(),
        high_threshold=int(high_threshold.get()),
        high_bet_type=high_bet_type.get()
    ).execute()


root = tk.Tk()
root.title("8u.com Bot")
canvas = tk.Canvas(root, width=600, height=300)

# Credentials
Label(root, text="Credentials", font=('Helvetica', 14, 'bold')).grid(row=1, pady=10)

Label(root, text="Username").grid(row=2)
username = Entry(root)
username.grid(row=2, column=1)
username.insert(0, "flovo94")

Label(root, text="Password").grid(row=3)
password = Entry(root)
password.grid(row=3, column=1)
password.insert(0, "Aa1234567890")

# Settings
Label(root, text="Settings", font=('Helvetica', 14, 'bold')).grid(row=4, pady=10)

Label(root, text="game_name").grid(row=5)
game_name = Entry(root)
game_name.grid(row=5, column=1)
game_name.insert(0, "CQK3M")

Label(root, text="minutes").grid(row=6)
minutes = Entry(root)
minutes.grid(row=6, column=1)
minutes.insert(0, 3)

Label(root, text="history_length").grid(row=7)
history_length = Entry(root)
history_length.grid(row=7, column=1)
history_length.insert(0, 10)

Label(root, text="initial_bet_amount").grid(row=8)
initial_bet_amount = Entry(root)
initial_bet_amount.grid(row=8, column=1)
initial_bet_amount.insert(0, 0.50)

Label(root, text="loss_multiplicator").grid(row=9)
loss_multiplicator = Entry(root)
loss_multiplicator.grid(row=9, column=1)
loss_multiplicator.insert(0, 3)

Label(root, text="low_threshold").grid(row=10)
low_threshold = Entry(root)
low_threshold.grid(row=10, column=1)
low_threshold.insert(0, -10)

Label(root, text="low_bet_type").grid(row=11)
low_bet_type = Entry(root)
low_bet_type.grid(row=11, column=1)
low_bet_type.insert(0, "big")

Label(root, text="high_threshold").grid(row=12)
high_threshold = Entry(root)
high_threshold.grid(row=12, column=1)
high_threshold.insert(0, 10)

Label(root, text="high_bet_type").grid(row=12)
high_bet_type = Entry(root)
high_bet_type.grid(row=12, column=1)
high_bet_type.insert(0, "small")

Button(root, text='Execute', command=execute_bot).grid(row=13, column=1, sticky=W, pady=4)

root.mainloop()

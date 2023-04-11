import tkinter as tk
from tkinter import ttk
import game


class GameStartWindow:

    def __init__(self, master):
        self.master = master
        master.title("Cosmic Defender")

        # Create name field
        self.name_label = ttk.Label(master, text="Name: ")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_field = ttk.Entry(master)
        self.name_field.grid(row=0, column=1, padx=10, pady=10)

        # Create checkbox group for spaceship
        self.option_label = ttk.Label(master, text="Select your space buddy:")
        self.option_label.grid(row=2, column=0, padx=10, pady=10)
        self.spaceship = tk.StringVar()
        self.option_1_checkbox = ttk.Checkbutton(
            master, text="spaceship 1", variable=self.spaceship, onvalue="1")
        self.option_1_checkbox.grid(row=2, column=1, padx=10, pady=10)
        self.option_2_checkbox = ttk.Checkbutton(
            master, text="spaceship 2", variable=self.spaceship, onvalue="2")
        self.option_2_checkbox.grid(row=3, column=1, padx=10, pady=10)
        self.option_3_checkbox = ttk.Checkbutton(
            master, text="spaceship 3", variable=self.spaceship, onvalue="3")
        self.option_3_checkbox.grid(row=4, column=1, padx=10, pady=10)

        # Create checkbox group for level difficulty
        self.level_label = ttk.Label(master, text="Select level difficulty:")
        self.level_label.grid(row=5, column=0, padx=10, pady=10)
        self.level_var = tk.StringVar()
        self.level_1_checkbox = ttk.Checkbutton(
            master, text="Easy", variable=self.level_var, onvalue="1")
        self.level_1_checkbox.grid(row=5, column=1, padx=10, pady=10)
        self.level_2_checkbox = ttk.Checkbutton(
            master, text="Medium", variable=self.level_var, onvalue="2")
        self.level_2_checkbox.grid(row=6, column=1, padx=10, pady=10)
        self.level_3_checkbox = ttk.Checkbutton(
            master, text="Hard", variable=self.level_var, onvalue="3")
        self.level_3_checkbox.grid(row=7, column=1, padx=10, pady=10)

        # Create Start button
        self.start_button = ttk.Button(
            master, text="Start", command=self.start_game)
        self.start_button.grid(row=8, column=1, padx=10, pady=10)

    def start_game(self):
        name = self.name_field.get()
        spaceship_no = int(self.spaceship.get())
        level = int(self.level_var.get())
        root.withdraw()
        game.main(name, spaceship_no, level)
        root.quit()


root = tk.Tk()
game_start_window = GameStartWindow(root)
root.mainloop()

import tkinter as tk
import time
from tkinter import messagebox

def update_time():
    current_time = time.strftime('%H:%M:%S')  
    time_label.config(text=current_time)     
    root.after(1000, update_time)             

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)

def exit_app():
    root.destroy()

def about():
    messagebox.showinfo("About", "This is a digital clock app.")

root = tk.Tk()
root.title("Digital Clock")

# Configure clock background colors
background_colors = ['black', 'navy', 'purple', 'darkgreen', 'maroon', 'darkslategray']
background_index = 0

def change_background_color():
    global background_index
    background_index = (background_index + 1) % len(background_colors)
    time_label.config(bg=background_colors[background_index])

# Creating a label to display the time
time_label = tk.Label(root, font=('Times New Roman', 80), fg='lime', bg='black')
time_label.pack(padx=20, pady=20)

# Creating a button to toggle fullscreen mode
fullscreen_button = tk.Button(root, text="Toggle Fullscreen", command=toggle_fullscreen)
fullscreen_button.pack(pady=10)

# Creating a button to change the clock background color
color_button = tk.Button(root, text="Change Color", command=change_background_color)
color_button.pack(pady=10)

menu_bar = tk.Menu(root)

# Creating a "File" menu with "Exit" option
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Creating a "Help" menu with "About" option
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
fullscreen = False
update_time() 
root.mainloop()
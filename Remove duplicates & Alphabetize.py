import tkinter as tk
from tkinter import filedialog, messagebox
import os



"""
 ____________________________________________________________________________________ 
|          _               _              _          _                      _        |
|        /\ \             _\ \           /\ \       /\_\                   /\ \      |
|       /  \ \           /\__ \         /  \ \     / / /         _        /  \ \____ |
|      / /\ \ \         / /_ \_\       / /\ \ \    \ \ \__      /\_\     / /\ \_____\|
|     / / /\ \ \       / / /\/_/      / / /\ \ \    \ \___\    / / /    / / /\/___  /|
|    / / /  \ \_\     / / /          / / /  \ \_\    \__  /   / / /    / / /   / / / |
|   / / /    \/_/    / / /          / / /   / / /    / / /   / / /    / / /   / / /  |
|  / / /            / / / ____     / / /   / / /    / / /   / / /    / / /   / / /   |
| / / /________    / /_/_/ ___/\  / / /___/ / /    / / /___/ / /     \ \ \__/ / /    |
|/ / /_________\  /_______/\__\/ / / /____\/ /    / / /____\/ /       \ \___\/ /     |
|\/____________/  \_______\/     \/_________/     \/_________/         \/_____/      |
|         _   _                 _       _      _               _               _     |
|       /\_\/\_\ _            /\ \   /_/\    /\ \            /\ \            /\ \    |
|      / / / / //\_\          \ \ \  \ \ \   \ \_\          /  \ \          /  \ \   |
|     /\ \/ \ \/ / /          /\ \_\  \ \ \__/ / /         / /\ \ \        / /\ \ \  |
|    /  \____\__/ /          / /\/_/   \ \__ \/_/         / / /\ \_\      / / /\ \_\ |
|   / /\/________/          / / /       \/_/\__/\        / /_/_ \/_/     / / /_/ / / |
|  / / /\/_// / /          / / /         _/\/__\ \      / /____/\       / / /__\/ /  |
| / / /    / / /          / / /         / _/_/\ \ \    / /\____\/      / / /_____/   |
|/ / /    / / /       ___/ / /__       / / /   \ \ \  / / /______     / / /\ \ \     |
|\/_/    / / /       /\__\/_/___\     / / /    /_/ / / / /_______\   / / /  \ \ \    |
|        \/_/        \/_________/     \/_/     \_\/  \/__________/   \/_/    \_\/    |
|                                                                                    |
|-------------------"Thank you Cloud but that's not very nice"-----------------------|
|____________________________________________________________________________________| 

"""





def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, file)

def process_file():
    file_path = entry_file_path.get()
    output_path = entry_output_path.get()
    if not file_path or not output_path:
        messagebox.showerror("Error", "Please select a file and specify the output file path.")
        return

    remove_duplicates = check_remove_dups_var.get()
    alphabetize = check_alphabetize_var.get()

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if remove_duplicates:
            lines = list(set(lines))

        if alphabetize:
            lines.sort()

        with open(output_path, 'w') as file:
            file.writelines(lines)

        messagebox.showinfo("Success", f"File has been processed and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="File Path:").grid(row=0, column=0, sticky='e')
entry_file_path = tk.Entry(frame, width=50)
entry_file_path.grid(row=0, column=1)
button_load_file = tk.Button(frame, text="Browse", command=load_file)
button_load_file.grid(row=0, column=2)

tk.Label(frame, text="Output File Path:").grid(row=1, column=0, sticky='e')
entry_output_path = tk.Entry(frame, width=50)
entry_output_path.grid(row=1, column=1)
button_save_file = tk.Button(frame, text="Browse", command=save_file)
button_save_file.grid(row=1, column=2)

check_remove_dups_var = tk.BooleanVar()
check_remove_dups = tk.Checkbutton(frame, text="Remove Duplicates", variable=check_remove_dups_var)
check_remove_dups.grid(row=2, column=1, sticky='w')

check_alphabetize_var = tk.BooleanVar()
check_alphabetize = tk.Checkbutton(frame, text="Alphabetize", variable=check_alphabetize_var)
check_alphabetize.grid(row=3, column=1, sticky='w')

button_process = tk.Button(frame, text="Process File", command=process_file)
button_process.grid(row=4, column=1, pady=10)

root.mainloop()
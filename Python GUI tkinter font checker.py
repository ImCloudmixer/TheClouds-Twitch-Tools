from tkinter import *
from tkinter.ttk import *
from tkinter import font

 
root = Tk()
root.title("Font Customization Magic")
root.geometry("500x300")   

 
font_list = list(font.families())


def choose_font(event):
    selected_font = font_option.get()    
    custom_font_data = font.Font(family=f'{selected_font}', size=30, weight='bold', slant='italic', underline=1, overstrike=0)
    display_label.config(font=custom_font_data)

 
font_option = Combobox(root, values=font_list, state='readonly')
font_option.pack(pady=10)

 
font_option.bind('<<ComboboxSelected>>', choose_font)

 
display_label = Label(root, text='Hello Font Magic!', font=('Arial', 12))   
display_label.pack(pady=20)

 
root.mainloop()
import tkinter
import tkinter.font
import customtkinter
import configparser
from pyglet import font as pyglet_font
import os


# Settings, later will be loadable from .ini file via ConfigParser
ACCENT_COLOR = "#bf2222"
ACCENT_COLOR_DARK = "#8f2424"


# Set up CustomTkinter
customtkinter.set_appearance_mode("dark")

# Initialize the window
root_tk = customtkinter.CTk()
root_tk.geometry("1000x600")
root_tk.title("Kart Racing Pro Manager")
'''root_tk.iconbitmap("Graphics\\krpmanager_icon.ico")'''
root_tk.resizable(False, False)
root_tk.configure(fg_color="#232323")

# Set the font
pyglet_font.add_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphics\\Fonts"))
large_font = tkinter.font.Font(family="serpentine_sans_icg", size=30)
small_font = tkinter.font.Font(family="serpentine_sans_icg", size=12)

# Initialize tab selector frame and the different selected tab frames
tab_frame_tk = customtkinter.CTkFrame(master=root_tk, width=980, height=40, corner_radius=5)
settings_frame_tk = customtkinter.CTkFrame(master=root_tk, width=980, height=530, corner_radius=5)

# Place them correctly
tab_frame_tk.place(x=10, y=10, width=980, height=40)
settings_frame_tk.place(x=10, y=60, width=980, height=530)

# Change their colors
tab_frame_tk.configure(fg_color="#404040")
settings_frame_tk.configure(fg_color="#404040")

# Spawn the tabs
tab_button_settings = customtkinter.CTkButton(master=tab_frame_tk, text="Settings", width=90, height=30, text_font=small_font, fg_color=ACCENT_COLOR, hover_color=ACCENT_COLOR_DARK)

# List them for quick organization
tabs_list = [tab_button_settings]

# Organize the tabs
for index_number, tab_name in enumerate(tabs_list):
    tab_name.grid(column=index_number, row=0, pady=5, padx=5)

# Start the GUI
root_tk.mainloop()
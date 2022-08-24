import tkinter
import tkinter.font
import customtkinter
import configparser
from pyglet import font as pyglet_font
import os


# Settings, later will be loadable from .ini file via ConfigParser
ACCENT_COLOR = "#cf1717"
ACCENT_COLOR_DARK = "#8a0f0f"
WINDOW_SIZE_X = 1200
WINDOW_SIZE_Y = 700
UI_PADDING = 10
UI_CORNER_RADIUS = 5
UI_TAB_HEIGHT = 40


# Set up CustomTkinter
customtkinter.set_appearance_mode("dark")

# Initialize the window
root_tk = customtkinter.CTk()
root_tk.geometry("{x_size}x{y_size}".format(x_size=WINDOW_SIZE_X, y_size=WINDOW_SIZE_Y))
root_tk.title("Kart Racing Pro Manager")
'''root_tk.iconbitmap("Graphics\\krpmanager_icon.ico")'''
root_tk.resizable(False, False)
root_tk.configure(fg_color="#232323")

# Set the font
pyglet_font.add_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Graphics\\Fonts"))
large_font = tkinter.font.Font(family="serpentine_sans_icg", size=30)
small_font = tkinter.font.Font(family="serpentine_sans_icg", size=12)

# Initialize tab selector frame and the different selected tab frames
tab_frame_tk = customtkinter.CTkFrame(master=root_tk, width=WINDOW_SIZE_X-(UI_PADDING*2), height=UI_TAB_HEIGHT, corner_radius=UI_CORNER_RADIUS)
settings_frame_tk = customtkinter.CTkFrame(master=root_tk, width=WINDOW_SIZE_X-(UI_PADDING*2), height=WINDOW_SIZE_Y-UI_TAB_HEIGHT-(UI_PADDING*3), corner_radius=UI_CORNER_RADIUS)

# Place them correctly
tab_frame_tk.place(x=UI_PADDING, y=UI_PADDING, width=WINDOW_SIZE_X-(UI_PADDING*2), height=UI_TAB_HEIGHT)
settings_frame_tk.place(x=UI_PADDING, y=60, width=WINDOW_SIZE_X-(UI_PADDING*2), height=WINDOW_SIZE_Y-UI_TAB_HEIGHT-(UI_PADDING*3))

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

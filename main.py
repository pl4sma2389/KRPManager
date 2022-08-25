import dearpygui.dearpygui as dpg
import win32con
from webcolors import hex_to_rgb
from webbrowser import open_new as connect_to_webpage
import configparser
import os
import win32gui
from win32com.shell import shell, shellcon
import threading
from time import sleep


# Variables
krp_was_running = False
app_window_pointer = None
self_window_pointer = None
folder_structure = None


# Settings initial load and config file creation with defaults if there isn't one yet
config = configparser.ConfigParser()
config.read("Settings\\settings.ini")
try:
    print("The current Mods directory is: {0}".format(config["DIRECTORIES"]["PIBOSO_KRP_MODS_DIRECTORY"]))
except:
    print("The current Mods directory could not be found. Creating new config file...")
    config["DIRECTORIES"] = {"PIBOSO_KRP_MODS_DIRECTORY": str(os.path.join(shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0), 'PiBoSo\\Kart Racing Pro\\Mods'))}
    config["COLORS"] = {"BACK_COLOR": "#232323",
                        "BACK_COLOR_LIGHT": "#232323",
                        "ACCENT_COLOR": "#cf1717",
                        "ACCENT_COLOR_DARK": "#8a0f0f"}
    config["WINDOW"] = {"WINDOW_SIZE_X": "1200",
                        "WINDOW_SIZE_Y": "700"}
    config["TIMING"] = {"SLEEP_SECS_WHILE_START_WAIT": "0.1",
                        "SLEEP_SECS_WHILE_RUN_WAIT": "2"}
    config["UI"] = {"UI_CORNER_RADIUS": "3",
                    "UI_FONT_SIZE_REGULAR": "20",
                    "UI_FONT_SIZE_SMALL": "15",
                    "UI_FONT_SIZE_LARGE": "25",
                    "UI_FONT_SIZE_HEADING": "30",
                    "UI_FONT_SIZE_TITLE": "40",
                    "UI_SCROLLBAR_SIZE": "16"}
    with open("Settings\\settings.ini", "w") as configfile:
        config.write(configfile)


# Enable easier reading of the settings
SETS_DIRECTORIES = config["DIRECTORIES"]
SETS_COLORS = config["COLORS"]
SETS_WINDOW = config["WINDOW"]
SETS_TIMING = config["TIMING"]
SETS_UI = config["UI"]


# Functions
def update_ui_positioning():  # Updates the position of certain UI elements, is called on window resize
    dpg.set_item_pos("bottom_buttons", [10, dpg.get_viewport_height()-75])
    for tab in UI_INTERNAL_TAB_1_CHILD_WINDOWS_LIST:
        dpg.set_item_height(tab, dpg.get_viewport_height() - 150)
    for tab in UI_INTERNAL_TAB_2_CHILD_WINDOWS_LIST:
        dpg.set_item_height(tab, dpg.get_viewport_height()-118)


def launch_krp():  # Launches KRP, then pops up a dialog box saying KRP is being launched. The viewport should minimize when kart.exe is found to be running, and the dialog should cancel and the viewport should restore when KRP is no longer found to be running.
    global krp_was_running
    if check_for_krp():  # Check if KRP is already running, and if so, don't launch it again.
        print("Cannot launch KRP, it's already running.")
    else:
        connect_to_webpage("steam://rungameid/415600")
        print("Launching KRP...")

    try:
        with dpg.window(tag="popup_waiting_for_krp", modal=True, no_title_bar=True, no_resize=True, pos=[int(dpg.get_viewport_width() / 2 - 155), int(dpg.get_viewport_height() / 2 - 75)]):
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=10)
                dpg.add_text("Launching KRP, please wait...")
                dpg.add_spacer(width=10)

            with dpg.group(horizontal=True):
                dpg.add_spacer(width=25)
                help_text = dpg.add_text("  If KRP does not launch within\na few seconds, please check Steam")

            dpg.add_spacer(height=10)

            with dpg.group(horizontal=True):
                dpg.add_spacer(width=100)
                dpg.add_button(label="Back", width=75, callback=lambda: dpg.configure_item("popup_waiting_for_krp", show=False))

            dpg.bind_item_font(help_text, small_font)
    except:
        dpg.configure_item("popup_waiting_for_krp", show=True)

    def minimize_self_upon_launch():
        global krp_was_running
        global self_window_pointer
        print("Running minimize_self_upon_launch")

        while True:

            if not krp_was_running:
                if check_for_krp():
                    print("Minimize routine started")
                    self_window_pointer = win32gui.FindWindow(None, "KRPManager")
                    print("Found window at", self_window_pointer)
                    win32gui.ShowWindow(self_window_pointer, win32con.SW_MINIMIZE)
                    dpg.configure_item("popup_waiting_for_krp", show=False)
                sleep(float(SETS_UI["SLEEP_SECS_WHILE_START_WAIT"]))

            if krp_was_running:
                if not check_for_krp():
                    print("Restore routine started")
                    win32gui.ShowWindow(self_window_pointer, win32con.SW_RESTORE)
                    krp_was_running = False
                    break
                sleep(float(SETS_UI["SLEEP_SECS_WHILE_RUN_WAIT"]))

    THREAD_krp_checker = threading.Thread(target=minimize_self_upon_launch())
    THREAD_krp_checker.start()


def check_for_krp():  # Checks for the presence of a "Kart Racing Pro" window and returns true if one exists, also logs the past presence of a KRP window with krp_was_running
    global app_window_pointer
    global krp_was_running

    if win32gui.FindWindow(None, "Kart Racing Pro"):
        print("Check: Kart Racing Pro IS running!")
        krp_was_running = True
        return True
    else:
        print("Check: Kart Racing Pro is NOT running!")
        return False


def load_mods_folder_structure():
    print("Loading directory structure of {0}...".format(SETS_DIRECTORIES["PIBOSO_KRP_MODS_DIRECTORY"]))
    os.scandir(SETS_DIRECTORIES["PIBOSO_KRP_MODS_DIRECTORY"])
    print("Directory structure loaded.")


# DPG init stuff
dpg.create_context()
dpg.create_viewport(title='KRPManager', width=int(SETS_WINDOW["WINDOW_SIZE_X"]), height=int(SETS_WINDOW["WINDOW_SIZE_Y"]), min_width=700, min_height=500)
dpg.set_viewport_vsync(True)
dpg.set_viewport_large_icon(icon="Graphics\\KRPManager_logo_256x.ico")
dpg.set_viewport_small_icon(icon="Graphics\\KRPManager_logo_32x.ico")


# Internal settings, these are not to be adjustable by the user
UI_INTERNAL_TEXT_ABOUT = "Developed by pl4sma2389 at Slip Angle Modding and Development\n\nThe following software, libraries, and assets are used in this program:\n\n" \
                         "Python 3.10: https://www.python.org/\n\tDear PyGui 1.6.2: https://github.com/hoffstadt/DearPyGui\n\twebcolors 1.3: https://github.com/ubernostrum/webcolors\n\n" \
                         "Roboto Mono: https://fonts.google.com/specimen/Roboto+Mono"
UI_INTERNAL_TAB_1_CHILD_WINDOWS_LIST = ["tracks_tab_child_window", "karts_tab_child_window", "skins_tab_child_window"]
UI_INTERNAL_TAB_2_CHILD_WINDOWS_LIST = ["settings_tab_child_window", "about_tab_child_window"]


# Register fonts and their sizes
with dpg.font_registry():
    regular_font = dpg.add_font("Graphics\\Fonts\\RobotoMono-SemiBold.ttf", int(SETS_UI["UI_FONT_SIZE_REGULAR"]))
    small_font = dpg.add_font("Graphics\\Fonts\\RobotoMono-SemiBold.ttf", int(SETS_UI["UI_FONT_SIZE_SMALL"]))
    large_font = dpg.add_font("Graphics\\Fonts\\RobotoMono-SemiBold.ttf", int(SETS_UI["UI_FONT_SIZE_LARGE"]))
    heading_font = dpg.add_font("Graphics\\Fonts\\Serpentine Sans ICG Bold.ttf", int(SETS_UI["UI_FONT_SIZE_HEADING"]))
    title_font = dpg.add_font("Graphics\\Fonts\\Serpentine Sans ICG Bold.ttf", int(SETS_UI["UI_FONT_SIZE_TITLE"]))


# Set up theme and colors
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, hex_to_rgb(SETS_COLORS["BACK_COLOR"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, hex_to_rgb(SETS_COLORS["BACK_COLOR_LIGHT"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, hex_to_rgb(SETS_COLORS["ACCENT_COLOR"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, hex_to_rgb(SETS_COLORS["ACCENT_COLOR_DARK"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, hex_to_rgb(SETS_COLORS["ACCENT_COLOR"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, hex_to_rgb(SETS_COLORS["ACCENT_COLOR_DARK"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 5, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 12, 4, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, int(SETS_UI["UI_CORNER_RADIUS"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_TabRounding, int(SETS_UI["UI_CORNER_RADIUS"]), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, int(SETS_UI["UI_SCROLLBAR_SIZE"]), category=dpg.mvThemeCat_Core)


# Lay out DPG window and all UI elements
with dpg.window(tag="Main Window"):
    with dpg.tab_bar():
        with dpg.tab(label="Manage"):
            with dpg.tab_bar():
                with dpg.tab(label="Tracks"):
                    with dpg.child_window(tag="tracks_tab_child_window", height=dpg.get_viewport_height() - 118):
                        window_heading = dpg.add_text("Track Management")
                        dpg.add_text("Track Management will go here")
                        dpg.bind_font(regular_font)
                        dpg.bind_item_font(window_heading, heading_font)

                with dpg.tab(label="Karts"):
                    with dpg.child_window(tag="karts_tab_child_window", height=dpg.get_viewport_height() - 118):
                        window_heading = dpg.add_text("Karts Management")
                        dpg.add_text("Karts Management will go here")
                        dpg.bind_font(regular_font)
                        dpg.bind_item_font(window_heading, heading_font)

                with dpg.tab(label="Skins"):
                    with dpg.child_window(tag="skins_tab_child_window", height=dpg.get_viewport_height() - 118):
                        window_heading = dpg.add_text("Skins Management")
                        dpg.add_text("Skins Management will go here")
                        dpg.bind_font(regular_font)
                        dpg.bind_item_font(window_heading, heading_font)

        with dpg.tab(label="Settings"):
            with dpg.child_window(tag="settings_tab_child_window", height=dpg.get_viewport_height() - 118):
                dpg.add_text("Settings will go here")

        with dpg.tab(label="About"):
            with dpg.child_window(tag="about_tab_child_window", height=dpg.get_viewport_height()-118):
                window_title = dpg.add_text("KRPManager")
                dpg.add_text(UI_INTERNAL_TEXT_ABOUT)
                dpg.bind_font(regular_font)
                dpg.bind_item_font(window_title, title_font)

    with dpg.group(tag="bottom_buttons", horizontal=True, pos=[10, dpg.get_viewport_height() - 75]):
        dpg.add_button(label="Launch KRP", callback=launch_krp)
        dpg.add_button(label="Rescan Installed Mods", callback=load_mods_folder_structure)


# Finalize DPG stuff
dpg.bind_theme(global_theme)
# dpg.show_style_editor()
# dpg.show_imgui_demo()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main Window", True)
dpg.set_viewport_resize_callback(update_ui_positioning)

# Start the GUI
dpg.start_dearpygui()

# Clean up after exit
dpg.destroy_context()

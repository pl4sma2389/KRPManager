import dearpygui.dearpygui as dpg
import webcolors as wc
import configparser
import os


# Settings, later will be loadable from .ini file via ConfigParser
BACK_COLOR = "#232323"
BACK_COLOR_LIGHT = "#232323"
ACCENT_COLOR = "#cf1717"
ACCENT_COLOR_DARK = "#8a0f0f"
WINDOW_SIZE_X = 1200
WINDOW_SIZE_Y = 700
UI_CORNER_RADIUS = 3
UI_FONT_SIZE_REGULAR = 20
UI_FONT_SIZE_LARGE = 25
UI_FONT_SIZE_HEADING = 30
UI_FONT_SIZE_TITLE = 40


dpg.create_context()
dpg.create_viewport(title='KRPManager', width=WINDOW_SIZE_X, height=WINDOW_SIZE_Y, min_width=700, min_height=500)
dpg.set_viewport_vsync(True)


# Register fonts and their sizes
with dpg.font_registry():
    regular_font = dpg.add_font("Graphics\\Fonts\\RobotoMono-SemiBold.ttf", UI_FONT_SIZE_REGULAR)
    large_font = dpg.add_font("Graphics\\Fonts\\RobotoMono-SemiBold.ttf", UI_FONT_SIZE_LARGE)
    heading_font = dpg.add_font("Graphics\\Fonts\\Serpentine Sans ICG Bold.ttf", UI_FONT_SIZE_HEADING)
    title_font = dpg.add_font("Graphics\\Fonts\\Serpentine Sans ICG Bold.ttf", UI_FONT_SIZE_TITLE)


# Set up theme and colors
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, wc.hex_to_rgb(BACK_COLOR), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, wc.hex_to_rgb(BACK_COLOR_LIGHT), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, wc.hex_to_rgb(ACCENT_COLOR), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, wc.hex_to_rgb(ACCENT_COLOR_DARK), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, wc.hex_to_rgb(ACCENT_COLOR), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, wc.hex_to_rgb(ACCENT_COLOR_DARK), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, UI_CORNER_RADIUS, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_TabRounding, UI_CORNER_RADIUS, category=dpg.mvThemeCat_Core)


with dpg.window(tag="Main Window"):
    with dpg.tab_bar():
        with dpg.tab(label="Manage"):
            with dpg.tab_bar():
                with dpg.tab(label="Tracks"):
                    window_heading = dpg.add_text("Track Management")
                    dpg.add_text("Track Management will go here")
                    dpg.bind_font(regular_font)
                    dpg.bind_item_font(window_heading, heading_font)

                with dpg.tab(label="Karts"):
                    window_heading = dpg.add_text("Karts Management")
                    dpg.add_text("Karts Management will go here")
                    dpg.bind_font(regular_font)
                    dpg.bind_item_font(window_heading, heading_font)

                with dpg.tab(label="Skins"):
                    window_heading = dpg.add_text("Skins Management")
                    dpg.add_text("Skins Management will go here")
                    dpg.bind_font(regular_font)
                    dpg.bind_item_font(window_heading, heading_font)

        with dpg.tab(label="Settings"):
            dpg.add_text("Settings will go here")

        with dpg.tab(label="About"):
            window_title = dpg.add_text("KRPManager")
            dpg.add_text("Developed by pl4sma2389 at Slip Angle Modding and Development\n\nThe following software and libraries are used in this program:\n\nPython 3.10\n\tDear PyGui 1.6.2\n\twebcolors 1.3")
            dpg.bind_font(regular_font)
            dpg.bind_item_font(window_title, title_font)

    with dpg.group(label="Always Available Buttons", horizontal=True, pos=(10, dpg.get_viewport_height()-75)):
        dpg.add_button(label="Launch KRP")
        dpg.add_button(label="Rescan Installed Mods")

    dpg.bind_font(regular_font)


dpg.bind_theme(global_theme)
# dpg.show_style_editor()
# dpg.show_imgui_demo()
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("Main Window", True)

dpg.start_dearpygui()

dpg.destroy_context()

# < Import modules >
import tkinter as tk
import itertools
import csv
import importlib
import os
import sys

# < Keeps animation window below everything and above desktop >
def send_to_back(_event=None):
    root.lower()

# < Updates the text continuously >
def update():
    label.config(text=next(cycle))
    root.after(int(config_dict["ms_delay"]), update)

# < Creates the config file >
def config_initialize():
    with open(config_path,'w') as csvfile:
        writer = csv.writer(csvfile)
        Config = [
            ["run", "Y"],
            ["animation_module", "ANIM_default"],
            ["ms_delay","200"],
            ["#1", "Use hex codes for colours"],
            ["background_colour", "#FFFFFF"],
            ["font","Consolas"],
            ["font_colour", "#000000"],
            ["#2", "Adjust taskbar_height according to your need"],
            ["taskbar_height", "48"]
        ]
        writer.writerows(Config)

# < Calls config file creation if it doesn't exist >
try:
    config_path = os.path.join(os.path.dirname(__file__), "config.csv")
    f = open(config_path, "r")
    f.close()
except FileNotFoundError:
    config_initialize()

# < Reads config settings >
with open(config_path,'r') as configfile:
    reader = csv.reader(configfile)
    config_dict = {row[0]: row[1] for row in reader if len(row) == 2}

# < Gets the frames module and defaults in case of error >
animations_path = os.path.join(os.path.dirname(__file__), "Animations")
if animations_path not in sys.path:
    sys.path.append(animations_path)

module_name = config_dict["animation_module"]
try:
    animation_module = importlib.import_module(module_name)
except ModuleNotFoundError:
    animation_module = importlib.import_module("ANIM_default")

# < Main() >
if config_dict["run"] == "Y":

    # < Create tkinter root >
    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(bg=config_dict["background_colour"])

    # < Kills the animation >
    root.bind("<Escape>", lambda e: root.destroy())  

    # < Manages position and size of the window; do not recommend changing >
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight() - int(config_dict["taskbar_height"])
    width = screen_w // 3
    height = screen_h
    x = (2 * screen_w) // 3
    y = 0
    root.geometry(f"{width}x{height}+{x}+{y}")

    # < Forces the window down >
    root.lower()
    root.bind("<FocusIn>", send_to_back)

    # < Running the actual animation >
    cycle = itertools.cycle(animation_module.frames)
    try:
        label = tk.Label(
            root, 
            font=(config_dict["font"], 20), 
            bg = config_dict["background_colour"], 
            fg = config_dict["font_colour"])
    except:
        label = tk.Label(root, font=("Consolas", 20), bg = "#000000", fg = "#FFFFFF")
    label.pack()
    update()
    root.mainloop()
    
else:
    pass

# -*- coding: utf-8 -*-
"""
@author: Hamedvolca
"""
import tkinter as tk
from PIL import Image, ImageTk
import screeninfo
import os

def center_window(window, width, height):
    screen = screeninfo.get_monitors()[0]
    screen_width = screen.width
    screen_height = screen.height
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def create_overlay(image_path):
    # Create the main window
    root = tk.Tk()
    root.title("Overlay Image")

    # To make a frameless window
    root.overrideredirect(True)

    # Load the image
    image = Image.open(image_path)
    img_width, img_height = image.size
    photo = ImageTk.PhotoImage(image)
    
    # Create a label with the image
    label = tk.Label(root, image=photo, bg='black')
    label.image = photo  # Keep a reference to the image to prevent garbage collection
    label.pack()

    # Center the window on the screen
    center_window(root, img_width, img_height)

    # Set the window to be stay above all (topmost)
    root.attributes('-topmost', True) 
    root.attributes('-alpha', 0.6)  # transparency level (0.0 to 1.0)
    root.wm_attributes('-transparentcolor','black') # transpanet image

    # Function to stop the code 
    def close_overlay(event=None):
        root.destroy()
    
    root.bind('<Escape>', close_overlay) # Escape key to close 
    root.bind('<Shift-Button-3>', close_overlay) # Shift+Right click on the image to close 

    # Allow click-through (on Windows, using `ctypes`)
    try:
        import ctypes
        root.update_idletasks()
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        ex_style |= 0x00000020  # WS_EX_TRANSPARENT
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style)
    except ImportError:
        pass

    root.mainloop()

# Path to the working directory
path_wd = 'C:/Users/' # Change this to your python working directory
os.chdir(path_wd)
# Path to the image
image_path = "target2.png"
create_overlay(image_path)

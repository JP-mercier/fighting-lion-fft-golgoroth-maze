# pip install numpy pillow keyboard scipy pywin32
import numpy as np
from PIL import Image, ImageGrab
import time
import keyboard
import scipy.signal
import win32api
import win32con
import win32com.client

# /Join Golg Maze CP#9613

x_start = int(1950 - 100)
y_start = int(658 - 100)

x_end = int(1950 + 100)
y_end = int(658 + 100)

# Keybind for the trigger
keyboard.wait("h")

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
time.sleep(.3)
ref_img = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end)).convert("L")  # X1,Y1,X2,Y2
# ref_img = ref_img.save("ref_img.png")
ref_img = np.array(ref_img)
ref_img = ref_img.astype(np.float64)
ref_img -= np.mean(ref_img)
shell = win32com.client.Dispatch("WScript.Shell")

# Add a flag to control the loop
running = True

def stop_script(e):
    global running
    running = False

# Set up a hotkey to stop the script
print("Press 'h' to start the script")
keyboard.on_press_key("h", stop_script)

while running:

    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)

    # Shoot
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.01)
    shell.SendKeys("a")
    shell.SendKeys("d")

    # wait for things to calm down then grab the current image
    time.sleep(3.7)  # Sleep for 3.7 seconds
    current_image = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end)).convert("L")
    
    # current_image = current_image.save("current_image.png") # Saves the current image
    current_image = np.array(current_image)
    current_image = current_image.astype(np.float64)
    current_image -= np.mean(current_image)

    # Convolve both images using Fast Fourier Transform
    corr_img = scipy.signal.fftconvolve(current_image, ref_img[::-1, ::-1], mode='same')
    
    # Normalization to 0-255 (Only if you want to display the convolved image)
    # corr_img *= (255.0/corr_img.max())
    # data = Image.fromarray(corr_img)
    # data.show()
    print(np.unravel_index(np.argmax(corr_img), corr_img.shape))
    shift = np.unravel_index(np.argmax(corr_img), corr_img.shape) # The brightest pixel /largest value is the "real center"
    # the difference between the coordinate of the "real center" and [100,100], which is the "true center", is the shift
    # Move mouse in the opposite direction of the shift
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, shift[1] - 100, shift[0] - 100, 0, 0)
    time.sleep(0.625)
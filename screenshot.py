import pyautogui
import datetime
import os
import time

from tkinter import filedialog, Tk

def take_screenshot():

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    default_filename = f"screenshot_{timestamp}.png"

    root = Tk()
    root.withdraw()

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialfile=default_filename,
        filetypes=[("PNG Files", "*.png")]
    )

    if save_path:
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)
        print(f"✅ Screenshot saved to: {save_path}")
    else:
        print("❌ Save cancelled.")

if __name__ == "__main__":
    print("📸 Screenshot Tool")
    input("Press Enter to take a screenshot...")
    take_screenshot()


if save_path:
    print("⏳ Taking screenshot in 3 seconds...")
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    print(f"✅ Screenshot saved to: {save_path}")

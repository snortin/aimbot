from pyautogui import *
import pyautogui, keyboard as kb
import win32api as api, win32con

# tile 1 / X: 567 Y: 400 / RGB: 79, 83, 116
# tile 2 / X: 644 Y: 400 / RGB: 78, 81, 116
# tile 3 / X: 729 Y: 400 / RGB: 82, 85, 116
# tile 4 / X: 808 Y: 400 / RGB: 85, 87, 116

def tap(X, Y):
    api.SetCursorPos((X, Y))
    api.api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 , 0)
    api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while kb.is_pressed('a') == False:
    if pyautogui.pixel(567, 400) [0] == 0:
        click(567, 400)
    if pyautogui.pixel(644, 400) [0] == 0:
        click(644, 400)
    if pyautogui.pixel(729, 400) [0] == 0:
        click(729, 400)
    if pyautogui.pixel(808, 400) [0] == 0:
        click(808, 400)
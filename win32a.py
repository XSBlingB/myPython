import win32gui
import win32api
import win32con
from win32gui import *
import time

from PIL import Image
from PIL import ImageGrab
import imagehash
import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
titles = set()


def foo(hwnd, mouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        titles.add(GetWindowText(hwnd))


def playGame():
    """Click the game icon in the simulator to enter and displays to the specified location"""
    EnumWindows(foo, 0)
    list = []
    for title in titles:
        if title:
            list.append(title)
    for title in list:
        a = '夜神模拟器'
        if title.find(a) != -1:
            hwnd = win32gui.FindWindow(0, a)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 640, 360, win32con.SWP_SHOWWINDOW)
            hwnd = win32gui.FindWindow(0, a)
            size = win32gui.GetWindowRect(hwnd)
            # 在模拟器点击游戏图标进入游戏
            win32api.SetCursorPos([size[0] + 410, size[1] + 186])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            time.sleep(10)
            return size


def game():
    """Click to implement in the game"""

    # 点击我知道
    size = playGame()
    time.sleep(15)
    topx, topy = size[0], size[1]
    ImageGrab.grab((topx + 287, topy + 307, topx + 350, topy + 330)).save('D:\ ceshi.jpg')
    hash_size = 6
    hash1 = imagehash.average_hash(Image.open('D:\ ceshi.jpg'), hash_size=hash_size)
    hash2 = imagehash.average_hash(Image.open('D:\我知道了.jpg'), hash_size=hash_size)
    a = (1 - (hash1 - hash2) / len(hash1.hash) ** 2)
    print(a)
    if a > 0.6:
        win32api.SetCursorPos([topx + 290, topy + 310])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)


if __name__ == '__main__':
    pass

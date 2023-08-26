import time, os
import ctypes
import threading
from ctypes import wintypes

class Button:
    A = 65 
    B = 66 
    C = 67 
    D = 68 
    E = 69 
    F = 70 
    G = 71 
    H = 72 
    I = 73 
    J = 74 
    K = 75 
    L = 76 
    M = 77 
    N = 78 
    O = 79 
    P = 80 
    Q = 81 
    R = 82 
    S = 83 
    T = 84 
    U = 85 
    V = 86 
    W = 87 
    X = 88 
    Y = 89 
    Z = 90 
    LEFT_ARROW = 37
    RIGHT_ARROW = 39
    DOWN_ARROW = 40
    UP_ARROW = 38
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    DEL = 46
    HOME = 36
    END = 35
    PGUP = 33
    PGDOWN = 34
    INSERT = 45
    LEFT_CTRL = 162
    RIGHT_CTRL = 163
    LEFT_ALT = 164
    RIGHT_ALT = 165
    MINUS = 189
    PLUS = 187
    UNDERSCORE = 189
    EQUALS = 187
    FORWARD_SLASH = 191
    BACK_SLASH = 220
    PIPE = 220
    EXCLAMATION_MARK = 33
    ASPERAND = 64
    RIGHT_ANGLE_BRACKET = 190
    LEFT_ANGLE_BRACKET = 188
    UP_ANGLE_BRACKET = 94
    SEMICOLON = 186
    COLON = 186
    SINGLE_QUOTE = 222
    DOUBLE_QUOTE = 222
    PERIOD = 190
    COMMA = 188
    QUESTION_MARK = 63
    RIGHT_BRACKET = 221
    LEFT_BRACKET = 219
    RIGHT_CURLY = 221
    LEFT_CURLY = 219
    HASHTAG = 35
    DOLLAR_SIGN = 36
    PERCENT_SIGN = 37
    AMPERSAND = 38
    ASTERISK = 42

def buttonenum_to_button(button):
    if button == Button.A:
        return ord('A')
    elif button == Button.B:
        return ord('B')
    elif button == Button.C:
        return ord('C')
    elif button == Button.D:
        return ord('D')
    elif button == Button.E:
        return ord('E')
    elif button == Button.F:
        return ord('F')
    elif button == Button.G:
        return ord('G')
    elif button == Button.H:
        return ord('H')
    elif button == Button.I:
        return ord('I')
    elif button == Button.J:
        return ord('J')
    elif button == Button.K:
        return ord('K')
    elif button == Button.L:
        return ord('L')
    elif button == Button.M:
        return ord('M')
    elif button == Button.N:
        return ord('N')
    elif button == Button.O:
        return ord('O')
    elif button == Button.P:
        return ord('P')
    elif button == Button.Q:
        return ord('Q')
    elif button == Button.R:
        return ord('R')
    elif button == Button.S:
        return ord('S')
    elif button == Button.T:
        return ord('T')
    elif button == Button.U:
        return ord('U')
    elif button == Button.V:
        return ord('V')
    elif button == Button.W:
        return ord('W')
    elif button == Button.X:
        return ord('X')
    elif button == Button.Y:
        return ord('Y')
    elif button == Button.Z:
        return ord('Z')
    elif button == Button.LEFT_ARROW:
        return 37
    elif button == Button.RIGHT_ARROW:
        return 39
    elif button == Button.DOWN_ARROW:
        return 40
    elif button == Button.UP_ARROW:
        return 38
    elif button == Button.F1:
        return 112
    elif button == Button.F2:
        return 113
    elif button == Button.F3:
        return 114
    elif button == Button.F4:
        return 115
    elif button == Button.F5:
        return 116
    elif button == Button.F6:
        return 117
    elif button == Button.F7:
        return 118
    elif button == Button.F8:
        return 119
    elif button == Button.F9:
        return 120
    elif button == Button.F10:
        return 121
    elif button == Button.F11:
        return 122
    elif button == Button.F12:
        return 123
    elif button == Button.DEL:
        return 46
    elif button == Button.HOME:
        return 36
    elif button == Button.END:
        return 35
    elif button == Button.PGUP:
        return 33
    elif button == Button.PGDOWN:
        return 34
    elif button == Button.INSERT:
        return 45
    elif button == Button.LEFT_CTRL:
        return 162
    elif button == Button.RIGHT_CTRL:
        return 163
    elif button == Button.LEFT_ALT:
        return 164
    elif button == Button.RIGHT_ALT:
        return 165
    elif button == Button.MINUS:
        return 189
    elif button == Button.PLUS:
        return 187
    elif button == Button.UNDERSCORE:
        return 189
    elif button == Button.EQUALS:
        return 187
    elif button == Button.FORWARD_SLASH:
        return 191
    elif button == Button.BACK_SLASH:
        return 220
    elif button == Button.PIPE:
        return 220
    elif button == Button.EXCLAMATION_MARK:
        return 33
    elif button == Button.ASPERAND:
        return 64
    elif button == Button.RIGHT_ANGLE_BRACKET:
        return 190
    elif button == Button.LEFT_ANGLE_BRACKET:
        return 188
    elif button == Button.UP_ANGLE_BRACKET:
        return 94
    elif button == Button.SEMICOLON:
        return 186
    elif button == Button.COLON:
        return 186
    elif button == Button.SINGLE_QUOTE:
        return 222
    elif button == Button.DOUBLE_QUOTE:
        return 222
    elif button == Button.PERIOD:
        return 190
    elif button == Button.COMMA:
        return 188
    elif button == Button.QUESTION_MARK:
        return 63
    elif button == Button.RIGHT_BRACKET:
        return 221
    elif button == Button.LEFT_BRACKET:
        return 219
    elif button == Button.RIGHT_CURLY:
        return 221
    elif button == Button.LEFT_CURLY:
        return 219
    elif button == Button.HASHTAG:
        return 35
    elif button == Button.DOLLAR_SIGN:
        return 36
    elif button == Button.PERCENT_SIGN:
        return 37
    elif button == Button.AMPERSAND:
        return 38
    elif button == Button.ASTERISK:
        return 42
    return 45  

toggle_button = None
toggle_button_str = None

robloxHWND = None
isEnabled = False

mode = 1

isRightClickPressed = False
rememberedCursorPos = wintypes.POINT(0, 0)

def updateRobloxHWND():
    global robloxHWND
    while True:
        currentHWND = ctypes.windll.user32.GetForegroundWindow()
        if currentHWND:
            getTitle = getWindowTitle(currentHWND)
            if getTitle == "Roblox" and currentHWND != robloxHWND:
                robloxHWND = currentHWND
                print("Roblox-HWND updated:", robloxHWND)
        time.sleep(5)

def isRbxActive():
    return ctypes.windll.user32.GetForegroundWindow() == robloxHWND

def getWindowTitle(handle):
    title = ctypes.create_unicode_buffer(32)
    ctypes.windll.user32.GetWindowTextW(handle, title, 32)
    return title.value

def fixCursor(handle):
    global mode
    if mode == 1:
        rect = wintypes.RECT()
        if ctypes.windll.user32.GetWindowRect(robloxHWND, ctypes.byref(rect)):
            sizeX = rect.right - rect.left
            sizeY = rect.bottom - rect.top
            centerX = (rect.right - rect.left) // 2
            centerY = (rect.bottom - rect.top) // 2
            
            ctypes.windll.user32.SetCursorPos(rect.left + centerX, rect.top + centerY)
    elif mode == 2:
        p = wintypes.POINT()
        if ctypes.windll.user32.GetCursorPos(ctypes.byref(p)):
            if ctypes.windll.user32.ScreenToClient(handle, ctypes.byref(p)):
                rect = wintypes.RECT()
                if ctypes.windll.user32.GetWindowRect(robloxHWND, ctypes.byref(rect)):
                    sizeX = rect.right - rect.left
                    sizeY = rect.bottom - rect.top
                    centerX = (rect.right - rect.left) // 2
                    centerY = (rect.bottom - rect.top) // 2
                    realP = wintypes.POINT()
                    if ctypes.windll.user32.GetCursorPos(ctypes.byref(realP)):
                        if p.x < 1:
                            ctypes.windll.user32.SetCursorPos(rect.left + 10, realP.y)
                        elif p.x > sizeX - 18:
                            ctypes.windll.user32.SetCursorPos(rect.right - 10, realP.y)
                        elif p.y < 35:
                            ctypes.windll.user32.SetCursorPos(realP.x, rect.top + 30)
                        elif p.y > sizeY - 10:
                            ctypes.windll.user32.SetCursorPos(realP.x, rect.bottom - 10)
    elif mode == 3:
        if ctypes.windll.user32.GetAsyncKeyState(0x02) & 0x8000:
            global isRightClickPressed
            if not isRightClickPressed:
                global rememberedCursorPos
                ctypes.windll.user32.GetCursorPos(ctypes.byref(rememberedCursorPos))
                isRightClickPressed = True
        else:
            if isRightClickPressed:
                ctypes.windll.user32.SetCursorPos(rememberedCursorPos.x, rememberedCursorPos.y)
                isRightClickPressed = False

        p = wintypes.POINT()
        if ctypes.windll.user32.GetCursorPos(ctypes.byref(p)):
            if ctypes.windll.user32.ScreenToClient(handle, ctypes.byref(p)):
                rect = wintypes.RECT()
                if ctypes.windll.user32.GetWindowRect(robloxHWND, ctypes.byref(rect)):
                    sizeX = rect.right - rect.left
                    sizeY = rect.bottom - rect.top
                    realP = wintypes.POINT()
                    if ctypes.windll.user32.GetCursorPos(ctypes.byref(realP)):
                        if isRightClickPressed and (realP.x != rememberedCursorPos.x or realP.y != rememberedCursorPos.y):
                            adjustedX = realP.x
                            adjustedY = realP.y
                            if adjustedX < rect.left:
                                adjustedX = rect.left
                            elif adjustedX > rect.right:
                                adjustedX = rect.right
                            if adjustedY < rect.top:
                                adjustedY = rect.top
                            elif adjustedY > rect.bottom:
                                adjustedY = rect.bottom
                            ctypes.windll.user32.SetCursorPos(adjustedX, adjustedY)
                        elif not isRightClickPressed:
                            if p.x < 1:
                                ctypes.windll.user32.SetCursorPos(rect.left + 10, realP.y)
                            elif p.x > sizeX - 18:
                                ctypes.windll.user32.SetCursorPos(rect.right - 10, realP.y)
                            elif p.y < 35:
                                ctypes.windll.user32.SetCursorPos(realP.x, rect.top + 30)
                            elif p.y > sizeY - 10:
                                ctypes.windll.user32.SetCursorPos(realP.x, rect.bottom - 10)

def init():
    global toggle_button, toggle_button_str, robloxHWND, isEnabled
    os.system("cls")
    print(f"Roblox-HWND: {robloxHWND}")
    print(f"Keybind: {toggle_button_str}")
    print(f"Enabled: {'Enabled' if isEnabled else 'Disabled'}")
    
    while robloxHWND is None:
        time.sleep(1)
    
    print("Roblox-HWND:", robloxHWND)
    
    print("Keybind:", toggle_button_str)
    print("Enabled:", "Enabled" if isEnabled else "Disabled")
    
def isRbxActive():
    return (ctypes.windll.user32.GetForegroundWindow() == robloxHWND)

def check():
    while True:
        if isRbxActive() and isEnabled:
            fixCursor(robloxHWND)
        time.sleep(0.01)
def toggle():
    while True:
        if ctypes.windll.user32.GetAsyncKeyState(toggle_button) != 0:
            global isEnabled
            isEnabled = not isEnabled
            os.system("cls")
            print(f"Roblox-HWND: {robloxHWND}")
            print(f"Keybind: {toggle_button_str}")
            print(f"Enabled: {'Enabled' if isEnabled else 'Disabled'}")
            time.sleep(1)
        time.sleep(0.025)

def string_to_button(button_str):
    button_dict = {
        "A": Button.A,
        "B": Button.B,
        "C": Button.C,
        "D": Button.D,
        "E": Button.E,
        "F": Button.F,
        "G": Button.G,
        "H": Button.H,
        "I": Button.I,
        "J": Button.J,
        "K": Button.K,
        "L": Button.L,
        "M": Button.M,
        "N": Button.N,
        "O": Button.O,
        "P": Button.P,
        "Q": Button.Q,
        "R": Button.R,
        "S": Button.S,
        "T": Button.T,
        "U": Button.U,
        "V": Button.V,
        "W": Button.W,
        "X": Button.X,
        "Y": Button.Y,
        "Z": Button.Z,
        "LEFT_ARROW": Button.LEFT_ARROW,
        "RIGHT_ARROW": Button.RIGHT_ARROW,
        "DOWN_ARROW": Button.DOWN_ARROW,
        "UP_ARROW": Button.UP_ARROW,
        "F1": Button.F1,
        "F2": Button.F2,
        "F3": Button.F3,
        "F4": Button.F4,
        "F5": Button.F5,
        "F6": Button.F6,
        "F7": Button.F7,
        "F8": Button.F8,
        "F9": Button.F9,
        "F10": Button.F10,
        "F11": Button.F11,
        "F12": Button.F12,
        "DEL": Button.DEL,
        "HOME": Button.HOME,
        "END": Button.END,
        "PGUP": Button.PGUP,
        "PGDOWN": Button.PGDOWN,
        "INSERT": Button.INSERT,
        "LEFT_CTRL": Button.LEFT_CTRL,
        "RIGHT_CTRL": Button.RIGHT_CTRL,
        "LEFT_ALT": Button.LEFT_ALT,
        "RIGHT_ALT": Button.RIGHT_ALT,
        "MINUS": Button.MINUS,
        "PLUS": Button.PLUS,
        "UNDERSCORE": Button.UNDERSCORE,
        "EQUALS": Button.EQUALS,
        "FORWARD_SLASH": Button.FORWARD_SLASH,
        "BACK_SLASH": Button.BACK_SLASH,
        "PIPE": Button.PIPE,
        "EXCLAMATION_MARK": Button.EXCLAMATION_MARK,
        "ASPERAND": Button.ASPERAND,
        "RIGHT_ANGLE_BRACKET": Button.RIGHT_ANGLE_BRACKET,
        "LEFT_ANGLE_BRACKET": Button.LEFT_ANGLE_BRACKET,
        "UP_ANGLE_BRACKET": Button.UP_ANGLE_BRACKET,
        "SEMICOLON": Button.SEMICOLON,
        "COLON": Button.COLON,
        "SINGLE_QUOTE": Button.SINGLE_QUOTE,
        "DOUBLE_QUOTE": Button.DOUBLE_QUOTE,
        "PERIOD": Button.PERIOD,
        "COMMA": Button.COMMA,
        "QUESTION_MARK": Button.QUESTION_MARK,
        "RIGHT_BRACKET": Button.RIGHT_BRACKET,
        "LEFT_BRACKET": Button.LEFT_BRACKET,
        "RIGHT_CURLY": Button.RIGHT_CURLY,
        "LEFT_CURLY": Button.LEFT_CURLY,
        "HASHTAG": Button.HASHTAG,
        "DOLLAR_SIGN": Button.DOLLAR_SIGN,
        "PERCENT_SIGN": Button.PERCENT_SIGN,
        "AMPERSAND": Button.AMPERSAND,
        "ASTERISK": Button.ASTERISK
    }
    return button_dict.get(button_str, Button.INSERT)


def config_toggle_key():
    global toggle_button, toggle_button_str
    while True:
        toggle_button_input = input("Enter the toggle key (e.g., F1, INSERT, A, B, ...): ").strip().upper()
        toggle_button = string_to_button(toggle_button_input)
        toggle_button_str = toggle_button_input

        with open("config.txt", "w") as config_file:
            config_file.write(toggle_button_str)

        print(f"Toggle key set to {toggle_button_str}")
        break
    
if __name__ == "__main__":
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as config_file:
            toggle_button_str = config_file.readline().strip()
            toggle_button = string_to_button(toggle_button_str)
    else:
        config_toggle_key()

    print("1. Force Center Lock\n2. Lock Border\n3. Remember Last Cursor Position Upon Dragging w/ Lock Border\n")
    mode = int(input("Input: "))

    if mode in [1, 2, 3]:
        ctypes.windll.kernel32.SetConsoleTitleA(b"MicrosoftRBX-CursorFix")
        init_thread = threading.Thread(target=init)
        check_thread = threading.Thread(target=check)
        toggle_thread = threading.Thread(target=toggle)
        update_thread = threading.Thread(target=updateRobloxHWND)
        init_thread.start()
        check_thread.start()
        toggle_thread.start()
        update_thread.start()
        init_thread.join()
        check_thread.join()
        toggle_thread.join()
        update_thread.join()
        input()
    else:
        print("Invalid option, please restart the software.")
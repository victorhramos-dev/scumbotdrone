import eel
import window
import pyautogui
import drone as dr
import subprocess
from win32api import GetSystemMetrics
import win32clipboard

# Set web files folder
eel.init('web')
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron.exe')

drone = dr.Drone()
sw = window.ScumWindow()

@eel.expose
def get_api_url():
    return 'http://scum.test/drone'

@eel.expose
def get_hwid():
    return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

@eel.expose
def get_game_state():
    return [sw.find_game(), [sw.x0, sw.y0, sw.x1, sw.y1]]

@eel.expose
def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

@eel.expose
def command(cmd):
    return eval(cmd)

options = {
    
}

eel.start('main.html', mode='electron', **options)
 
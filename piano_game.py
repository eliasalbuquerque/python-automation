# 202401 - Python 3.12.0
# 4.18 - Projeto 3 - Zerar Game Piano Titles com PyAutoGUI


import pyautogui
import keyboard
import webbrowser
import win32api
import win32con
from time import sleep


def abrir_jogo(endereco_jogo):
    webbrowser.open(endereco_jogo)
    sleep(3)
    pyautogui.click(1442,498, duration=1)

def comecar_jogo():
    sleep(1)
    pyautogui.click(1442,498)

def os_commands(*comando):
    pyautogui.hotkey(*comando)

def controles_do_jogo():
    # pontos de click do piano
    if pyautogui.pixelMatchesColor(1295,378, (0,0,0)):
        click(1295,378)
        # pyautogui.click()
    if pyautogui.pixelMatchesColor(1389,379, (0,0,0)):
        click(1389,379)
        # pyautogui.click()
    if pyautogui.pixelMatchesColor(1484,379, (0,0,0)):
        click(1484,379)
        # pyautogui.click()
    if pyautogui.pixelMatchesColor(1575,379, (0,0,0)):
        click(1575,379)
        # pyautogui.click()

def click(x, y):
    # win32 mouse control
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def reiniciar_jogo():
    sleep(.5)
    title = 'Game Piano'
    text = 'Deseja reiniciar o jogo?'
    buttons = ['Sim', 'Cancelar']
    confirmacao = pyautogui.confirm(text=text, title=title, buttons=buttons)
    return confirmacao

def jogando_o_jogo():
    while keyboard.is_pressed('esc') == False:
        controles_do_jogo()



def aplicacao():
    jogo = 'https://gameforge.com/en-US/littlegames/magic-piano-tiles/#'
    abrir_jogo(jogo)
    comecar_jogo()
    while keyboard.is_pressed('esc') == False:
        jogando_o_jogo()
        reiniciar = reiniciar_jogo()
        if reiniciar == 'Sim':
            comecar_jogo()
            jogando_o_jogo()
        else:
            break

aplicacao()
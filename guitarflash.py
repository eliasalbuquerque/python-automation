# 202401 - Python 3.12.0

import pyautogui
import keyboard
from time import sleep


def ativar_janela(x, y):
    sleep(.3)
    pyautogui.moveTo(x, y, duration=.5)

def scroll_janela(pixels):
    sleep(.3)
    pyautogui.scroll(pixels)
    pyautogui.click()

def iniciar_game():
    sleep(.3)
    pyautogui.click()
    pyautogui.press('space')
    jogando()

def reiniciar_game():
    sleep(.3)
    pyautogui.click(1431,485, duration=.5)
    jogando()

verde = (0,152,0)
vermelho = (255,0,0)
amarelo = (220,220,2)
azul = (0,152,255)

def controles_game():
    if pyautogui.pixelMatchesColor(1266,658,verde):
        pyautogui.press('a')
        sleep(.1)
    if pyautogui.pixelMatchesColor(1344,658,vermelho):
        pyautogui.press('s')
        sleep(.1)
    if pyautogui.pixelMatchesColor(1425,658,amarelo):
        pyautogui.press('j')
        sleep(.1)
    if pyautogui.pixelMatchesColor(1507,658,azul):
        pyautogui.press('k')
        sleep(.1)

def prompt_novo_jogo():
    sleep(.3)
    text = 'Jogar um novo jogo?'
    title = 'pyAutoGUI guitarflsh.com'
    buttons = 'Novo', 'Sair'
    novo_jogo = pyautogui.confirm(text=text, title=title, buttons=buttons)
    return novo_jogo

def jogando():
    while keyboard.is_pressed('1') == False:
        controles_game()

def iniciar_aplicacao():
    ativar_janela(1425,588)
    scroll_janela(-290)
    iniciar_game()
    novo_jogo = prompt_novo_jogo()    
    if novo_jogo == 'Novo':
        reiniciar_game()
    else:
        pyautogui.alert('Fim do jogo!')



iniciar_aplicacao()
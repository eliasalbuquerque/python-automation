# 202312 - Python 3.12.0


import pyautogui
import time
from pyautogui_criar_pasta import *


def verificando_pastas_no_diretorio():
    pastas_existentes = contar_pastas_no_diretorio(diretorio)

    while pastas_existentes < 2:
        criar_pasta()

        sucesso = criar_pasta()
        if not sucesso:
            break

        pastas_existentes = contar_pastas_no_diretorio(diretorio)


verificando_pastas_no_diretorio()


def inserindo_arquivos():
    for i in range(4):
        nome_arquivo = './assets/New folder (2)/Arquivo' + str(i) + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('Arquivo ' + str(i))


inserindo_arquivos()


def abrir_explorers():
    # abrir explorer
    pyautogui.click(1100,1049,duration=.5) 
    # ajustar janela a esquerda
    time.sleep(1)
    pyautogui.hotkey('win','left')
    # barra pesquisa
    pyautogui.click(684,80,duration=2)
    # abrir pasta
    pyautogui.write('C:/Users/elias/Workspace/python-automation/assets/New folder (2)')
    pyautogui.hotkey('enter')
    pyautogui.click(531,81,duration=1)
    # abrir explorer botao direito
    pyautogui.rightClick(1100,1049,duration=.5) 
    pyautogui.click(1090,893,duration=.5)
    # ajustar janela a direita
    time.sleep(1)
    pyautogui.hotkey('win','right')
    # barra de pesquisa
    pyautogui.click(1493,79,duration=2)
    # abrir segunda pasta
    pyautogui.write('C:/Users/elias/Workspace/python-automation/assets/New folder')
    pyautogui.hotkey('enter')
    pyautogui.click(1486,79,duration=2)


abrir_explorers()


def mover_arquivos():
    pyautogui.moveTo(488,237,duration=.5)
    pyautogui.dragTo(787,446,button='left',duration=1)
    pyautogui.moveTo(488,237,duration=.5)
    pyautogui.dragTo(1580,545,button='left',duration=1)


mover_arquivos()

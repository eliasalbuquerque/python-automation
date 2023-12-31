# 202312 - Python 3.12.0
# 4.9 - Como digitar em qualquer lugar


import pyautogui
import pyperclip
import keyboard
import time


colar_frase_chamada = False


def colar_frase(frase, acao="whatsapp"):
    global colar_frase_chamada
    colar_frase_chamada = True
    pyperclip.copy(frase)

    if acao == "whatsapp":
        messagem_whatsapp(frase)
    elif acao == "notepad":
        texto_notepad(frase)
    else:
        print(f"Invalid action: {acao}")


def mensagem(frase):
    if colar_frase_chamada:
        pyautogui.hotkey('ctrl', 'v')
    else:
        keyboard.write(frase, delay=.1)


def messagem_whatsapp(frase):
    pyautogui.click(1411, 30, duration=1)
    pyautogui.click(1665, 981, duration=1)
    mensagem(frase)
    pyautogui.click(1874, 981, duration=1)


def texto_notepad(frase):
    pyautogui.hotkey('win')
    pyautogui.click(955, 159, duration=.5)
    pyautogui.typewrite('notepad')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    mensagem(frase)


# Enviando mensagem pelo Whatsapp Web
# colar_frase('Olá! Mandando msg usando Python', 'whatsapp')
# messagem_whatsapp('Olá! Mandando msg usando Python')


# DESAFIO
# Crie um programa que vai até onde seu bloco de notas estiver aberto e digita a frase "Automação é Incrível"

# Colando a frase:
# colar_frase('Automação é Incrível', 'notepad')

# Digitando a frase:
texto_notepad('Automação é Incrível')

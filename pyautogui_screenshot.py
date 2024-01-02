# 202401 - Python 3.12.0
# 4.12 - Tirando prints da tela

import pyautogui
import time
import logging
import logging.config
import keyboard


# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)



def screenshot_calculadora():
    logging.info('INICIO: screenshot calculadora.')
    try:
        def largura_altura():
            # coordenadas do screenshot
            regiao_inicial = [1457, 188]
            regiao_final = [1855, 851]
            regiao = []

            # calcula largura e altura do screenshot
            largura = regiao_final[0] - regiao_inicial[0]
            altura = regiao_final[1] - regiao_inicial[1]

            # coordenadas do screenshot para argumento 'region'
            regiao.extend([regiao_inicial[0], regiao_inicial[1], largura, altura])
            logging.info('Coordenadas do screenshot inseridas.')
            return regiao

        regiao = largura_altura()
        pyautogui.screenshot('assets/screenshot1.jpg', region=regiao)
        logging.info('Screenshot salvo.')
    except Exception as e:
        logging.error(f"Erro ao tirar screenshot da calculadora: {e}")



# screenshot_calculadora()



def screenshot_notepad():
    logging.info('INICIO: screenshot notepad.')
    try:
        def abrindo_notepad(frase):
            pyautogui.hotkey('win')
            pyautogui.click(955, 159, duration=.5)
            pyautogui.typewrite('notepad')
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'n')
            time.sleep(1)
            keyboard.write(frase, delay=.1)
            logging.info('Notepad aberto.')

        abrindo_notepad('42')

        def salvando_screenshot():
            # obtendo janela ativa
            janela_ativa = pyautogui.getActiveWindow()

            # screenshot janela ativa
            screenshot = pyautogui.screenshot(region=(janela_ativa.left, janela_ativa.top, janela_ativa.width, janela_ativa.height))

            # salvando screenshot
            screenshot.save(r'assets/screenshot2.jpg')
            logging.info('Screenshot salvo.')

        salvando_screenshot()
    except Exception as e:
        logging.error(f"Erro ao tirar screenshot do notepad: {e}")



screenshot_notepad()

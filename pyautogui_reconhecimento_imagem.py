# 202401 - Python 3.12.0
# 4.13 - Como quebrar captcha com reconhecimento de imagem


import pyautogui
import logging
import logging.config


# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def localizando_calculadora():
    try:
        logging.info('INICIO: Localizando calculadora.')

        # encontrar coordenadas proximas da imagem
        print(pyautogui.locateOnScreen('assets/calc-botao-4.png'))
        print(pyautogui.locateOnScreen('assets/calc-botao-2.png'))

        # encontrar o centro das coordenadas de acordo com a imagem
        botao_4 = pyautogui.locateCenterOnScreen('assets/calc-botao-4.png')
        botao_2 = pyautogui.locateCenterOnScreen('assets/calc-botao-2.png')
        logging.info('Coordenadas salvas')

        pyautogui.click(botao_4, duration=1)
        pyautogui.click(botao_2, duration=1)
        logging.info('Movimento click executado.')

    except Exception as e:
        logging.error(f'Erro ao localizar a calculadora: {e}')
        pyautogui.alert('ERRO: Ocorreu um erro ao localizar a calculadora')


# if __name__ == '__main__':
    # localizando_calculadora()



def clicando_no_captcha():
    try:
        logging.info('INICIO: Clicando no captcha.')
        captcha = pyautogui.locateCenterOnScreen('assets/captcha.png')
        pyautogui.click(captcha, duration=1)
        logging.info('Captcha clicado.')

    except Exception as e:
        logging.error(f'Erro ao clicar no captcha: {e}', exc_info=True)
        pyautogui.alert('ERRO: Ocorreu um erro ao clicar no captcha')


if __name__ == '__main__':
    clicando_no_captcha()
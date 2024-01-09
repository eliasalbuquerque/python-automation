# 202401 - Python 3.12.0
# 4.19 - Projeto 4 - Bot de Envio de mensagem em massa no WhatsApp


import os
import webbrowser
import pyautogui
import logging
import logging.config
from decouple import config
from time import sleep


# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def enviar_mensagens_whatsapp_web():
    logging.info('INICIO: Enviando Mensagem WhatsApp.')

    # carregar configuracoes
    config('CONTATO_01')  # Activate loading

    # iterar por contatos no arquivo .env
    for key, value in os.environ.items():
        if key.startswith('CONTATO_'):
            contato_numero = value
            contato_url = f'https://api.whatsapp.com/send?phone={contato_numero}'

            # enviar mensagem
            try:
                webbrowser.open(contato_url)
                sleep(5)
                pyautogui.click(1429,338, duration=.5) # "continue to chat"
                sleep(3)
                pyautogui.click(1429,410, duration=.5) # "use whatsapp web"
                sleep(5)
                pyautogui.click(1596,980, duration=.5) # "type a message"
                sleep(3)
                pyautogui.typewrite('Ola programador!') # mensagem
                sleep(3)
                pyautogui.hotkey('enter') # botao "send"
                logging.info('abriu whatsapp e enviou mensagem.')

            except webbrowser.Error as e:
                logging.error(f'ERRO: ao abrir WhatsApp Web para {contato_numero}:\n- {type(e).__name__}: {e}')
                pyautogui.alert(f'ERRO: ao abrir WhatsApp Web para {contato_numero}')

            # delay anti-bot
            sleep(240)

if __name__ == '__main__':
    enviar_mensagens_whatsapp_web()

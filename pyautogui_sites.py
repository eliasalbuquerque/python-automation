# 202401 - Python 3.12.0
# 4.14 - Automação de sites com PyAutoGUI


import pyautogui
import webbrowser
import time
import logging
import logging.config


# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def open_facebook_site():
    logging.info('INICIO: Abrindo Facebook.')
    
    try:
        # open()
        # open_new_tab()
        # open_new()
        webbrowser.open('https://facebook.com')
        logging.info('Site aberto.')
    except Exception as e:
        logging.error(f'Erro ao acessar o site: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro acessar o site:: {e}', exc_info=True)


# if __name__ == '__main__':
#     open_facebook_site()




def abrir_site(site, https):
    try:
        webbrowser.open(https)
        logging.info('site aberto')
    except Exception as e:
        logging.error(f'ERRO: ao acessar o site {site}\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro acessar o site {site}')


def scroll_site(site):
    try:
        pyautogui.click(1436,129, duration=.5)
        logging.info('clicou no site para ativar a janela')
        
        time.sleep(1)
        pyautogui.scroll(-700)
        logging.info('desceu ate o campo "Exemplos Alertas"')

    except Exception as e:
        logging.error(f'ERRO: ao scrolar o site {site}\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro scrolar o site {site}')


def digite_seu_nome(nome):
    try:
        time.sleep(1)
        captcha = pyautogui.locateCenterOnScreen('assets/digite-seu-nome.png')
        pyautogui.click(captcha, duration=.5)
        pyautogui.write(nome)
        logging.info('digitou o nome no campo "Exemplos Alertas"')

    except Exception as e:
        logging.error(f'ERRO: ao digitar o nome\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro ao digitar o nome')


def abrir_fechar_alerta():
    try:
        captcha = pyautogui.locateCenterOnScreen('assets/clicar-alerta.png')
        pyautogui.click(captcha, duration=.5)
        logging.info('clicou no botao de alerta')
        
        time.sleep(1)
        pyautogui.hotkey('space')
        logging.info('fechou o alerta')

    except Exception as e:
        logging.error(f'ERRO: ao abrir e fechar alerta\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro ao abrir e fechar Alerta')
    

def sobe_desce():
    try:
        time.sleep(1)
        pyautogui.scroll(700)
        logging.info('subiu ate o inicio da pagina')

        time.sleep(1)
        pyautogui.scroll(-2000)
        logging.info('desceu até downloads de arquivos')

    except Exception as e:
        logging.error(f'ERRO: ao subir e descer a janela\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro ao subir e descer a janela')
  
    
def downlaod_arquivos():
    
    def download():
        try:
            captchas = ['assets/download-excel.png', 'assets/download-pdf.png']

            for captcha in captchas:
                time.sleep(1)
                posicao = pyautogui.locateCenterOnScreen(captcha)
                time.sleep(1)
                pyautogui.hotkey('esc')
                pyautogui.moveTo(posicao, duration=.5)
                x, y = posicao
                pyautogui.click(x, y + 42, duration=.5)
                time.sleep(1)
                pyautogui.hotkey('esc')
                
                # extraindo o tipo de arquivo a partir de string
                arquivo = captcha.split('/')[1].split('-')[1].split('.')[0]
                
                logging.info(f'download do arquivo {arquivo}')

        except Exception as e:
            logging.error(f'ERRO: ao fazer download dos arquivos\n- {type(e).__name__}: {e}')
            pyautogui.alert(f'ERRO: Ocorreu um erro ao fazer download dos arquivos')
        
    def mover_arquivos():
        try:
            time.sleep(1)
            pyautogui.hotkey('win', 'e')
            time.sleep(.5)
            pyautogui.hotkey('alt', 'd')
            time.sleep(.5)
            pyautogui.write('Downloads')
            time.sleep(.5)
            pyautogui.hotkey('enter')
            time.sleep(.5)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(.5)
            pyautogui.hotkey('ctrl', 'x')
            time.sleep(.5)
            pyautogui.hotkey('alt', 'd')
            time.sleep(.5)
            pyautogui.write('C:/Users/elias/Workspace/python-automation/assets')
            time.sleep(.5)
            pyautogui.hotkey('enter')
            time.sleep(.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)
            pyautogui.hotkey('enter')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            
            logging.info('arquivos movidos para a pasta assets')
        except Exception as e:
            logging.error(f'ERRO: ao mover arquivos\n- {type(e).__name__}: {e}')
            pyautogui.alert(f'ERRO: Ocorreu um erro ao mover arquivos')
        
    download()
    mover_arquivos()


def finalizando_script():
    try:
        time.sleep(.5)
        pyautogui.alert('VOCÊ TERMINOU APLICAÇÃO')
        logging.info('alerta de finalizacao executado')
    except Exception as e:
        logging.error(f'ERRO: ao emitir alerta de finalizacao\n- {type(e).__name__}: {e}')
        pyautogui.alert(f'ERRO: Ocorreu um erro ao emitir o alerta de finalizacao')
    
    


# DESAFIO
# 1) Navegue até o site https://cursoautomacao.netlify.app/
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas"
#    e digite seu nome
# 3) Clique em alerta, para gerar a alerta
# 4) Feche a alerta
# 5) Suba a página totalmente para cima
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os
#    arquivos para o quais irá fazer o download e click no botão de download
#    para realizar o downlaod dos arquivos excel e pdf.
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
# APLICACAO:

site = 'cursoautomacao'
endereco = 'https://cursoautomacao.netlify.app/'
nome = 'Elias Albuquerque'

try:
    logging.info('START APPLICATION...')

    # args: nome do site, endereco do site
    if __name__ == '__main__':
        abrir_site(site, endereco)
        scroll_site(site)
        digite_seu_nome(nome)
        abrir_fechar_alerta()
        sobe_desce()
        downlaod_arquivos()
        finalizando_script()
    
    logging.info('END APPLICATION')

except Exception as e:
    logging.error(f'ERRO: ao rodar a aplicacao:\n- {type(e).__name__}: {e}')
    pyautogui.alert(f'ERRO: Ocorreu um erro ao digitar o nome')

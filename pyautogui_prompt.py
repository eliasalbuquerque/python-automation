# 202401 - Python 3.12.0
# 4.11 - Como mostrar alertas e pegar dados do usuário para automatizar algo


import pyautogui
import logging
import logging.config
import pyperclip
import time
import os



def confirmar_deletar():
    title = 'Alerta! Deletar'
    text = 'Deseja realmente deletar esse arquivo?'
    buttons = ['Sim', 'Cancelar']

    confirmacao = pyautogui.confirm(text=text, title=title, buttons=buttons)

    if confirmacao == 'Sim':
        print('Deletando arquivo')
    else:
        print('Cancelando ação')


# confirmar_deletar()


def digitar_senha():
    title = 'Senha'
    text = 'Digite a sua senha:'
    mask = '*'

    senha = pyautogui.password(text=text, title=title, mask=mask)

    if senha:
        print(f'Senha {senha} salva')
    else:
        print('Cancelando ação')


# digitar_senha()


# DESAFIO
# Crie um programa que pede o usuário e senha e, na sequência, copie e cole 
# o usuário e senha dentro de um bloco de notas

# configurando logging:
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


# solicitar usuario e senha
def usuario_senha():
    text_usuario = 'Digite seu usuário:'
    text_senha = 'Digite sua senha:'
    title = 'Login'
    mask = '*'

    usuario = pyautogui.prompt(text=text_usuario, title=title)
    logger.info('Usuário solicitado')

    senha = pyautogui.password(text=text_senha, title=title)
    logger.info('Senha solicitada')

    return usuario, senha



# salvar no bloco de notas
def salvar_dados(conteudo):

    def salvando_novo_arquivo():
        with open('assets/dados-usuario.txt', 'w', encoding='utf-8', newline='') as arquivo:
            arquivo.write(conteudo + os.linesep)

    def adicionando_novos_dados():
        with open('assets/dados-usuario.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(conteudo + os.linesep)

    def verifica_arquivo():
        arquivo = './assets/dados-usuario.txt'

        if os.path.isfile(arquivo):  
            try:
                adicionando_novos_dados()
                logging.info('Dados adicionados ao arquivo existente')
            except Exception as e:
                logging.error(f'Erro ao adicionar dados ao arquivo: {e}')
        else:
            try:
                salvando_novo_arquivo()
                logging.info('Novo arquivo criado e dados salvos')
            except Exception as e:
                logging.error(f'Erro ao criar novo arquivo e salvar dados: {e}')

    verifica_arquivo()


def salvar_usuario_local():    
    logging.info('1. INICIO:')

    usuario, senha = usuario_senha()
    
    title = 'Salvar usuário e senha'
    text = 'Deseja salvar usuário e senha em um arquivo local?'
    buttons = ['Sim', 'Cancelar']

    confirmacao = pyautogui.confirm(text=text, title=title, buttons=buttons)

    if confirmacao == 'Sim':
        logger.info('Usuário confirmou para salvar')
        dados = f'user: {usuario}, pass: {senha}'
        salvar_dados(dados)
    else:
        logger.info('Operação cancelada pelo usuário')
        pyautogui.alert('Operação cancelada!')


salvar_usuario_local()
"""
title: 'rpa_instagram'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-01-04'
update: '2024-01-05'
"""

import pyautogui
import webbrowser
import time
import random
import schedule


class RpaInstagram:

    def __init__(self, endereco):
        self.endereco = endereco

    def abrir_site(self):
        webbrowser.open(self.endereco)
        time.sleep(5)
        self.ativar_janela()

    def mover_mouse(self, x=None, y=None, imagem=None, click=False, duration=.5):
        time.sleep(1)
        if imagem is None and x is None and y is None:
            raise ValueError(
                "Pelo menos um dos parâmetros 'x', 'y' ou o caminho da 'imagem' deve ser fornecido")
        if imagem:
            x, y = self.coordenada_imagem(imagem)
        if click:
            time.sleep(.3)
            pyautogui.click(x, y, duration=duration)
        else:
            time.sleep(.3)
            pyautogui.moveTo(x, y, duration=duration)

    def coordenada_imagem(self, imagem):
        coordenada = pyautogui.locateCenterOnScreen(imagem)
        return coordenada

    def ativar_janela(self):
        ativar_janela = 1906, 147
        time.sleep(.3)
        self.mover_mouse(*ativar_janela)

    def scroll_site(self, valor_em_pixels):
        time.sleep(1)
        pyautogui.scroll(valor_em_pixels)

    def seguidor(self):
        time.sleep(1)
        seguindo = 'assets/seguindo-nike.png'
        seguir = 'assets/seguir-nike.png'
        try:
            time.sleep(.3)
            self.mover_mouse(imagem=seguir, click=True)
        except:
            if pyautogui.locateCenterOnScreen(seguindo) is not None:
                print("Ja eh um seguidor")
            else:
                raise ValueError(f"Image {imagem} not found on screen")

    def ultima_postagem(self):
        posts_referencia = 'assets/posts-nike.png'
        time.sleep(.3)
        self.mover_mouse(imagem=posts_referencia)
        pyautogui.move(-110, 130, duration=.5)
        pyautogui.click()

    def curtir_comentar_postagem(self, mensagem):
        time.sleep(1)
        curtir = 'assets/curtir-nike.png'
        curtida = 'assets/curtida-nike.png'
        try:
            time.sleep(.3)
            self.mover_mouse(imagem=curtir, click=True)
            self.postar_comentario(mensagem)
        except:
            if pyautogui.locateCenterOnScreen(curtida) is not None:
                print("postagem ja foi curtida e comentada")
            else:
                raise ValueError(f"Image {imagem} not found on screen")

    def postar_comentario(self, mensagem):
        add_comentario = 'assets/comentario-nike.png'
        postar = 'assets/portar-comentario-nike.png'

        # comentar
        time.sleep(1)
        self.mover_mouse(imagem=add_comentario, click=True)
        time.sleep(.3)
        pyautogui.write(mensagem)
        time.sleep(.3)
        pyautogui.hotkey('enter')
        self.foi_comentado = True

        # postar
        time.sleep(1)
        self.mover_mouse(imagem=add_comentario, click=True, duration=1.5)
        time.sleep(.5)
        pyautogui.hotkey('esc')

    def home_instagram(self):
        home = 'assets/home-instagram.png'
        time.sleep(.5)
        pyautogui.hotkey('esc')
        time.sleep(1)
        self.mover_mouse(imagem=home, click=True)


# APPLICACAO

endereco_da_pagina = 'https://www.instagram.com/nike/'

def rodando_aplicacao():
    rpa_instagram = RpaInstagram(endereco_da_pagina)

    # 1. abrir o Instagram
    rpa_instagram.abrir_site()

    # 2. buscar pela página
    # 3. verifica se é seguidor, se não, seguir
    rpa_instagram.seguidor()

    # 4. abrir postagem mais recente
    rpa_instagram.ultima_postagem()

    # 5. verifica se postagem já foi curtida, se não, curtir
    # 6. adicionar um comentário
    comentario = random.choice([
        'Showw!!',
        'Incrivel!',
        'Parabens!!!',
        'Bom trabalho!!'
    ])
    rpa_instagram.curtir_comentar_postagem(comentario)

    # 7. voltar para home do Instagram
    rpa_instagram.home_instagram()

# 8. repetir processo a cada 24h
schedule.every(24).hours.do(rodando_aplicacao)


print('inicio')
rodando_aplicacao()

time.sleep(2)

print('segunda vez rodando')
rodando_aplicacao()

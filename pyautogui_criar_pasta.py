# 202312 - Python 3.12.0


import pyautogui
import os
import logging



logging.basicConfig(level=logging.DEBUG, encoding='utf-8',
                    filename='log/criar_pasta.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')


def single_click(x, y):
    pyautogui.click(x, y, duration=1)


def double_click(x, y):
    pyautogui.doubleClick(x, y, duration=1)


def right_click(x, y):
    pyautogui.rightClick(x, y, duration=1)


def get_coordinates(file_path):
    coordenadas = {}
    with open(file_path, 'r') as file:
        for line in file:
            x, y, key = line.split(',')
            x, y = map(int, (x, y))
            coordenadas[key.strip()] = (x, y)
    return coordenadas


coordenadas = get_coordinates('coordenadas.txt')


def contar_pastas_no_diretorio(diretorio):
    return len(os.listdir(diretorio))


diretorio = './assets'
pastas_existentes = contar_pastas_no_diretorio(diretorio)


def criar_pasta():
    try:
        print('Abrindo diretório e criando pasta...')

        for key in coordenadas.keys():
            x, y = coordenadas[key]

            if 'single' in key:
                single_click(x, y)
            elif 'double' in key:
                double_click(x, y)
            elif 'right' in key:
                right_click(x, y)

        pastas_atualizadas = contar_pastas_no_diretorio(diretorio)

        if pastas_atualizadas > pastas_existentes:
            logging.info('Pasta criada no diretório "assets".')
            print('Pasta criada com sucesso!')
        else:
            logging.error('A nova pasta não foi criada no diretório "assets".')
            print('Não foi possível criar nova pasta.')
    except Exception as exception:
        logging.error(
            'Ocorreu um erro enquanto a nova pasta estava sendo criada')


if __name__ == '__main__':
    criar_pasta()

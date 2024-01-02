# 202312 - Python 3.12.0


import pyautogui

# movendo mouse com movimento de 2 segundos
pyautogui.moveTo(1343,400, duration=2)

# loop click
pyautogui.click(clicks=100)

# clicar na coordenada
pyautogui.click(1343,400)

# parametros de clicks
pyautogui.click(1343,400, clicks=100, interval=.1, button='left', duration=2)

# duplo click
pyautogui.doubleClick()

# click com o direito
pyautogui.rightClick()

# click com o do meio
pyautogui.middleClick()
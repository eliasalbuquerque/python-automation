# Automation with PyAutoGUI module

This repository is dedicated to the study and development of Python-based 
automation and most of the features are developed using the `pyautogui` module.


## Functions developed:

- click, drag and drop
- screen scrolling
- insert texts
- use prompts for information and interaction with the user
- image recognition
- save a screenshot of a specific region
- create directories and interact with operating system commands
- interaction projects with online games using mouse movement, clicks and 
  specific controls for each game
- automation project for likes and follows on Instagram
- Message automation project via WhatsApp web


## Other features:

- global logging configuration (config.ini) and log file
- dependencies requirements file
- error handling with `try/except`


# Project highlights


## Project 4 - WhatsApp Mass Messaging Bot

This is a Python script that automates the sending of mass messages on WhatsApp Web. Here is a brief description of the code:

1. **Module Importation**: The script imports several modules, including `os`, `webbrowser`, `pyautogui`, `logging`, `logging.config`, `decouple.config`, and `time`.

2. **Logging Configuration**: The script configures logging using a 'config.ini' file.

3. **Function `enviar_mensagens_whatsapp_web()`:** This function is responsible for sending messages on WhatsApp Web.
    - First, it loads the contact settings from the `.env` file.
    - Then, it iterates over all contacts in the `.env` file that start with 'CONTATO_'.
    - For each contact, it opens WhatsApp Web using the WhatsApp API URL.
    - Next, it uses the `pyautogui` module to simulate clicks and typing to send the message.
    - If an error occurs when opening WhatsApp Web, it will be logged and an alert will be displayed.
    - Finally, it waits 240 seconds before moving on to the next contact to avoid being detected as a bot.

4. **Script Execution**: If the script is run as the main script, it will call the `enviar_mensagens_whatsapp_web()` function to start the message sending process.


### Code

https://github.com/eliasalbuquerque/python-automation/blob/master/bot_whatsapp.py

### Final Result

<!-- insert screenshot or .gif -->
![whatsapp-messages](https://github.com/eliasalbuquerque/python-automation/assets/78819295/3677a9fe-a385-4b55-ab6c-f18238598f45)


---


## Instagram Likes and Comments Bot with PyAutoGUI:

Let's create a bot that determines which page it wants to follow, checks if the most recent post has not yet been liked by the bot. If a new post has been made, it should enter this post, like it, and comment something on it.

### Steps

1. open Instagram
2. search for the page
3. check if it is a follower, if not, follow
4. open the most recent post
5. check if the post has already been liked, if not, like
6. add a comment
7. return to Instagram home
8. repeat process every 24h

### Code

https://github.com/eliasalbuquerque/python-automation/blob/master/rpa_instagram.py


The program has methods to:

- open a website, in this specific case, Instagram;
- mouse actions:
  - move according to defined coordinates for `x` and `y`, or, using the method to extract coordinates from an image;
  - option to only move the mouse to a point or move and click;
- scroll the site (scroll);
- follow, open the last post, like and comment, if this process has not yet been done;
- return to the home of Instagram.


### Final Result and Terminal

<!-- insert screenshot or .gif -->
<!-- ![Alt text](automacao-instagram.gif) -->


---


## Challenge

1) Navigate to the website https://cursoautomacao.netlify.app/
2) Find and click on the field "Digite seu nome" within "exemplos Alertas" and type your name
3) Click on alert, to generate the alert
4) Close the alert
5) Scroll the page all the way up
6) Scroll down just enough to reach the section that contains the files for which you will download and click on the download button to download the excel and pdf files.
7) After you have done this, create an alert that says "VOCÊ TERMINOU"


### Code

https://github.com/eliasalbuquerque/python-automation/blob/master/pyautogui_sites.py


Added to the project:

- use of functions;
- list;
- string handling from items in a list;
- error handling;
- application log;


## Final Result

<!-- insert screenshot or .gif -->
<!-- ![Alt text](automacao-completa.gif) -->
![automacao-completa](https://github.com/eliasalbuquerque/python-automation/assets/78819295/55ced1e9-89a7-49d3-a566-04d41a4673da)


**Log:**

```Logtalk
2024-01-03 16:01:42,598 - root - INFO - START APPLICATION...
2024-01-03 16:01:42,657 - root - INFO - site aberto
2024-01-03 16:01:43,330 - root - INFO - clicou no site para ativar a janela
2024-01-03 16:01:46,434 - root - INFO - desceu ate o campo "Exemplos Alertas"
2024-01-03 16:01:47,476 - PIL.PngImagePlugin - DEBUG - STREAM b'IHDR' 16 13
2024-01-03 16:01:47,476 - PIL.PngImagePlugin - DEBUG - STREAM b'sRGB' 41 1
2024-01-03 16:01:47,476 - PIL.PngImagePlugin - DEBUG - STREAM b'gAMA' 54 4
2024-01-03 16:01:47,476 - PIL.PngImagePlugin - DEBUG - STREAM b'pHYs' 70 9
2024-01-03 16:01:47,476 - PIL.PngImagePlugin - DEBUG - STREAM b'iTXt' 91 95
2024-01-03 16:01:47,477 - PIL.PngImagePlugin - DEBUG - STREAM b'IDAT' 198 1093
2024-01-03 16:01:48,398 - root - INFO - digitou o nome no campo "Exemplos Alertas"
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'IHDR' 16 13
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'sRGB' 41 1
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'gAMA' 54 4
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'pHYs' 70 9
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'iTXt' 91 93
2024-01-03 16:01:48,429 - PIL.PngImagePlugin - DEBUG - STREAM b'IDAT' 196 604
2024-01-03 16:01:49,233 - root - INFO - clicou no botao de alerta
2024-01-03 16:01:50,335 - root - INFO - fechou o alerta
2024-01-03 16:01:51,437 - root - INFO - subiu ate o inicio da pagina
2024-01-03 16:01:52,538 - root - INFO - desceu até downlods de arquivos
2024-01-03 16:01:53,567 - PIL.PngImagePlugin - DEBUG - STREAM b'IHDR' 16 13
2024-01-03 16:01:53,568 - PIL.PngImagePlugin - DEBUG - STREAM b'sRGB' 41 1
2024-01-03 16:01:53,568 - PIL.PngImagePlugin - DEBUG - STREAM b'gAMA' 54 4
2024-01-03 16:01:53,568 - PIL.PngImagePlugin - DEBUG - STREAM b'pHYs' 70 9
2024-01-03 16:01:53,568 - PIL.PngImagePlugin - DEBUG - STREAM b'iTXt' 91 93
2024-01-03 16:01:53,568 - PIL.PngImagePlugin - DEBUG - STREAM b'IDAT' 196 1194
2024-01-03 16:01:57,222 - root - INFO - downloado do arquivo excel
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'IHDR' 16 13
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'sRGB' 41 1
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'gAMA' 54 4
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'pHYs' 70 9
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'iTXt' 91 93
2024-01-03 16:01:58,263 - PIL.PngImagePlugin - DEBUG - STREAM b'IDAT' 196 787
2024-01-03 16:02:01,896 - root - INFO - downloado do arquivo pdf
2024-01-03 16:02:12,654 - root - INFO - arquivos movidos para a pasta assets
2024-01-03 16:02:16,163 - root - INFO - alerta de finalizacao executado
2024-01-03 16:02:16,163 - root - INFO - END APPLICATION
```


---
[GitHub: eliasalbuquerque/python-automation](https://github.com/eliasalbuquerque/python-automation/tree/master)

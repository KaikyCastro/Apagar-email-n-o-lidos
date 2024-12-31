from pyautogui import click
from time import sleep
from keyboard import is_pressed

while True:
    # Verificar se a tecla ESC foi pressionada para interromper o loop
    if is_pressed("esc"):
        print("Loop interrompido pelo usuario!")
        break

    # Clicar na caixinha de expansão
    click(375, 217, duration=0.5)
    sleep(0.5)

    # Selecionar os emails não lidos
    click(469, 374, duration=0.5)
    sleep(0.5)

    # Apagar os emails não lidos
    click(536, 221, duration=0.5)
    sleep(0.5)

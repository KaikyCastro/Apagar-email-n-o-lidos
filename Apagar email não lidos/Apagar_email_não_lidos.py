import pyautogui
from time import sleep
import keyboard

while True:
    # Verificar se a tecla ESC foi pressionada para interromper o loop
    if keyboard.is_pressed("esc"):
        print("Loop interrompido pelo usuario!")
        break

    # Clicar na caixinha de expansão
    pyautogui.click(375, 217, duration=0.5)
    sleep(0.5)

    # Selecionar os emails não lidos
    pyautogui.click(469, 374, duration=0.5)
    sleep(0.5)

    # Apagar os emails não lidos
    pyautogui.click(536, 221, duration=0.5)
    sleep(0.5)

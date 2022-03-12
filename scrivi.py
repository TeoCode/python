from pynput.keyboard import Controller
import time

keyboard = Controller()

msg = input("Inserisci cosa scrivere: ")
print("Avvio...")
time.sleep(5)

for char in (msg):
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.01)

print("Scritta completata con successo!")
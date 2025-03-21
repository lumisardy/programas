import pyautogui
import time
from PIL import ImageGrab

def get_colors_around_cursor():
    # Obtiene la posición actual del cursor del ratón
    x, y = pyautogui.position()
    # Captura un área de 20x20 píxeles alrededor del cursor
    screen = ImageGrab.grab(bbox=(x-10, y-10, x+10, y+10))  # 20 píxeles (centro ±10 píxeles)
    colors = [screen.getpixel((i, j)) for i in range(20) for j in range(20)]  # Extrae colores de cada píxel en el área
    return colors

def is_green(color):
    # Define el rango para el color verde (ajustar según necesidad)
    r, g, b = color
    return g > 100 and r < 100 and b < 100

def main():
    print("Iniciando detección de color en área 20x20 alrededor del cursor...")
    time.sleep(3)  # Espera 3 segundos antes de empezar
    try:
        while True:
            colors = get_colors_around_cursor()
            if any(is_green(color) for color in colors):  # Comprueba si algún píxel es verde
                print("Color verde detectado en el área, haciendo clic...")
                pyautogui.click()  # Hace clic donde esté el ratón
                time.sleep(0.5)  # Espera medio segundo para evitar múltiples clics
            time.sleep(0.1)  # Espera un breve momento antes de volver a verificar
    except KeyboardInterrupt:
        print("Programa detenido.")

if __name__ == "__main__":
    main()

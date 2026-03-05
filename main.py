import mss
import cv2
import numpy as np


def captura_tela():
     with mss.mss() as sct:
        monitor = sct.monitors[1]  # Captura a tela principal
        frame = np.array(sct.grab(monitor))  # Captura a tela e converte para um array numpy
        return cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Converte de BGRA para BGR

if __name__ == "__main__":
   frame = captura_tela()
   cv2.imshow("Tela Capturada", frame)  # Exibe a tela capturada
   cv2.waitKey(0)  # Aguarda até que uma tecla seja pressionada
   cv2.destroyAllWindows()  # Fecha a janela exibida


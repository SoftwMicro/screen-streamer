import mss
import cv2
import numpy as np

def captura_tela():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Captura a tela principal
        cv2.namedWindow("Streming Local - captura de Tela", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Streming Local - captura de Tela", cv2.WND_PROP_TOPMOST, 1)
        while True:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            cv2.imshow("Streming Local - captura de Tela", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()  # Fecha a janela exibida

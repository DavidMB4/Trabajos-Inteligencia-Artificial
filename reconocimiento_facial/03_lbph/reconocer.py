import cv2 as cv
import os
import sys

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_RAIZ = os.path.dirname(DIR_ACTUAL)
CARPETA_DATASET = os.path.join(CARPETA_RAIZ, "dataset")
MODELO_XML = os.path.join(DIR_ACTUAL, "modelo_lbph.xml")

CASCADE_PATH = os.path.join(CARPETA_RAIZ, "haarcascade_frontalface_alt2.xml")
if not os.path.exists(CASCADE_PATH):
    CASCADE_PATH = cv.data.haarcascades + "haarcascade_frontalface_alt2.xml"

# Umbral para LBPH (segun apuntes del profesor: 70)
# En LBPH: menor distancia = mas parecido
THRESHOLD = 70

def main():
    global THRESHOLD

    if not os.path.exists(MODELO_XML):
        print(f"Error: No se encontro el modelo '{MODELO_XML}'")
        print("Ejecuta primero 'entrenar.py' en esta carpeta.")
        sys.exit(1)

    if not os.path.exists(CARPETA_DATASET):
        print(f"Error: No existe la carpeta {CARPETA_DATASET}")
        sys.exit(1)

    personas = sorted([
        d for d in os.listdir(CARPETA_DATASET)
        if os.path.isdir(os.path.join(CARPETA_DATASET, d))
    ])

    print("Personas:", personas)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(MODELO_XML)
    print("Modelo cargado correctamente.")

    cascade = cv.CascadeClassifier(CASCADE_PATH)
    if cascade.empty():
        print("Error al cargar clasificador Haar Cascade.")
        sys.exit(1)

    print("\nSelecciona origen:")
    print(" [0] Camara web")
    print(" [1] Video")
    opc = input("Opcion (0/1): ").strip()

    if opc == "1":
        ruta_video = input("Ruta del video: ").strip("\"' ")
        if not os.path.exists(ruta_video):
            posible = os.path.join(CARPETA_RAIZ, ruta_video)
            if os.path.exists(posible):
                ruta_video = posible
        cap = cv.VideoCapture(ruta_video)
    else:
        cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo abrir la camara o video.")
        sys.exit(1)

    print("Controles: [ESC] Salir | [+] Incrementar umbral | [-] Disminuir umbral")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        rostros = cascade.detectMultiScale(gray, 1.3, 3)

        for (x, y, w, h) in rostros:
            roi = cv.resize(gray[y:y + h, x:x + w], (100, 100), interpolation=cv.INTER_CUBIC)
            label_id, confidence = face_recognizer.predict(roi)

            if confidence < THRESHOLD and label_id < len(personas):
                nombre = personas[label_id]
                color = (0, 255, 0)
                texto = f"{nombre} ({confidence:.0f})"
            else:
                color = (0, 0, 255)
                texto = f"Desconocido ({confidence:.0f})"

            cv.putText(frame, texto, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv.LINE_AA)
            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        cv.putText(frame, f"Umbral: {THRESHOLD}", (15, 25), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)
        cv.imshow("LBPH", frame)

        tecla = cv.waitKey(1) & 0xFF
        if tecla == 27:
            break
        elif tecla == ord('+') or tecla == ord('='):
            THRESHOLD += 5
            print(f"Nuevo umbral: {THRESHOLD}")
        elif tecla == ord('-'):
            THRESHOLD = max(5, THRESHOLD - 5)
            print(f"Nuevo umbral: {THRESHOLD}")

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

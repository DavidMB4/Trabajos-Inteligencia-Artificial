import cv2 as cv
import numpy as np
import os
import sys
import threading
import time

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_RAIZ = os.path.dirname(DIR_ACTUAL)
CARPETA_DATASET = os.path.join(CARPETA_RAIZ, "dataset")
MODELO_XML = os.path.join(DIR_ACTUAL, "modelo_eigenfaces.xml")

def main():
    if not os.path.exists(CARPETA_DATASET):
        print(f"Error: No existe la carpeta {CARPETA_DATASET}")
        sys.exit(1)

    personas = sorted([
        d for d in os.listdir(CARPETA_DATASET)
        if os.path.isdir(os.path.join(CARPETA_DATASET, d))
    ])

    print("Personas:", personas)

    labels = []
    faces_data = []

    for label_id, persona in enumerate(personas):
        ruta_persona = os.path.join(CARPETA_DATASET, persona)
        archivos_img = sorted(os.listdir(ruta_persona))
        total_persona = 0

        for nombre_img in archivos_img:
            if not nombre_img.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            ruta_img = os.path.join(ruta_persona, nombre_img)
            img = cv.imread(ruta_img, 0)
            if img is None:
                continue

            if img.shape != (100, 100):
                img = cv.resize(img, (100, 100), interpolation=cv.INTER_CUBIC)

            labels.append(label_id)
            faces_data.append(img)
            total_persona += 1

        print(f"  {persona} (label={label_id}): {total_persona} fotos")

    if len(faces_data) == 0:
        print("Error: No hay imagenes para entrenar.")
        sys.exit(1)

    print("\nEntrenando modelo...")
    print(f"Total imagenes: {len(faces_data)}")

    tiempo_inicio = time.time()
    entrenando = True

    def monitor():
        while entrenando:
            time.sleep(300)
            if entrenando:
                segundos = int(time.time() - tiempo_inicio)
                minutos = segundos // 60
                seg = segundos % 60
                print(f"Entrenando... tiempo: {minutos}m {seg:02d}s", flush=True)

    hilo = threading.Thread(target=monitor, daemon=True)
    hilo.start()

    face_recognizer = cv.face.EigenFaceRecognizer_create()
    face_recognizer.train(faces_data, np.array(labels))
    entrenando = False

    t_total = int(time.time() - tiempo_inicio)
    print(f"Entrenamiento completado en {t_total // 60}m {t_total % 60}s")

    face_recognizer.write(MODELO_XML)
    print("Modelo guardado:", MODELO_XML)

if __name__ == "__main__":
    main()

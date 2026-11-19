import cv2 as cv
import os
import sys

# ==============================================================================
# SCRIPT 03: RECONOCIMIENTO FACIAL EN TIEMPO REAL (EIGENFACES)
# ==============================================================================
# Carga 'modelo_eigenfaces.xml' y detecta/reconoce rostros por Webcam o Video.
# En Eigenfaces: MENOR distancia (confidence) = MAYOR parecido.
# ==============================================================================

CARPETA_DATASET = os.path.join(os.path.dirname(__file__), "dataset")
MODELO_XML = os.path.join(os.path.dirname(__file__), "01_eigenfaces", "modelo_eigenfaces.xml")

CASCADE_PATH = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_alt2.xml")
if not os.path.exists(CASCADE_PATH):
    CASCADE_PATH = cv.data.haarcascades + "haarcascade_frontalface_alt2.xml"

# Umbral inicial de distancia (ajustable con las teclas '+' y '-' durante la ejecución)
# En Eigenfaces valores típicos rondan entre 2500 y 4500 dependiendo de la iluminación.
THRESHOLD = 3000


def main():
    global THRESHOLD
    print("=" * 60)
    print("  RECONOCIMIENTO FACIAL EN TIEMPO REAL (EIGENFACES)")
    print("=" * 60)

    # 1. Verificar existencia del modelo
    if not os.path.exists(MODELO_XML):
        print(f"❌ Error: No se encontró el modelo entrenado '{MODELO_XML}'.")
        print("Ejecuta primero '02_entrenar_eigenfaces.py'.")
        sys.exit(1)

    # 2. Cargar las clases (personas) desde el dataset para tener los mismos nombres e IDs
    if not os.path.exists(CARPETA_DATASET):
        print(f"❌ Error: Carpeta '{CARPETA_DATASET}' no encontrada.")
        sys.exit(1)

    personas = sorted([
        d for d in os.listdir(CARPETA_DATASET)
        if os.path.isdir(os.path.join(CARPETA_DATASET, d))
    ])

    if not personas:
        print("❌ Error: No se encontraron carpetas de personas en el dataset.")
        sys.exit(1)

    print(f"Clases registradas ({len(personas)}): {personas}")

    # 3. Cargar el reconocedor
    try:
        face_recognizer = cv.face.EigenFaceRecognizer_create()
    except AttributeError:
        print("❌ Error: No se encontró el módulo 'cv2.face'. Instala: pip install opencv-contrib-python")
        sys.exit(1)

    face_recognizer.read(MODELO_XML)
    print("✅ Modelo cargado correctamente.")

    # 4. Cargar Haar Cascade
    cascade = cv.CascadeClassifier(CASCADE_PATH)
    if cascade.empty():
        print("❌ Error al cargar Haar Cascade.")
        sys.exit(1)

    # 5. Iniciar cámara (o preguntar si desea video)
    print("\nSelecciona la fuente para reconocimiento:")
    print(" [0] Cámara Web (por defecto)")
    print(" [1] Archivo de video")
    opc = input("Opción (0/1): ").strip()

    if opc == "1":
        video_path = input("Ruta del archivo de video: ").strip("\"' ")
        cap = cv.VideoCapture(video_path)
    else:
        cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: No se pudo abrir la cámara o video.")
        sys.exit(1)

    print("\nControles:")
    print("  - [ESC]: Salir")
    print("  - [+]: Incrementar umbral (+100) (más permisivo)")
    print("  - [-]: Disminuir umbral (-100) (más estricto)")
    print("-" * 60)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fin del video o cámara desconectada.")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        rostros = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(60, 60))

        for (x, y, w, h) in rostros:
            # Recorte en escala de grises y redimensionado a 100x100
            roi = gray[y:y+h, x:x+w]
            roi_resized = cv.resize(roi, (100, 100), interpolation=cv.INTER_CUBIC)

            # Predicción con Eigenfaces
            label_id, confidence = face_recognizer.predict(roi_resized)

            # En Eigenfaces: MENOR distancia = MEJOR coincidencia
            if confidence < THRESHOLD and label_id < len(personas):
                nombre = personas[label_id]
                color = (0, 255, 0)  # Verde
                texto = f"{nombre} ({confidence:.0f})"
            else:
                color = (0, 0, 255)  # Rojo
                texto = f"Desconocido ({confidence:.0f})"

            # Dibujar etiqueta y rectángulo
            cv.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv.putText(frame, texto, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv.LINE_AA)

        # Barra superior con información del umbral
        cv.putText(frame, f"Umbral actual: {THRESHOLD}  [+/-]", (15, 25),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1, cv.LINE_AA)

        cv.imshow("Reconocimiento Facial - Eigenfaces", frame)

        tecla = cv.waitKey(1) & 0xFF
        if tecla == 27:  # ESC
            break
        elif tecla == ord('+') or tecla == ord('='):
            THRESHOLD += 100
            print(f"Nuevo umbral: {THRESHOLD}")
        elif tecla == ord('-'):
            THRESHOLD = max(100, THRESHOLD - 100)
            print(f"Nuevo umbral: {THRESHOLD}")

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

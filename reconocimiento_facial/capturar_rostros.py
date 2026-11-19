import cv2 as cv
import os
import sys

CARPETA_DATASET = os.path.join(os.path.dirname(__file__), "dataset")
CANTIDAD_FOTOS = 1000           
TAMANO_ROSTRO = (100, 100)      

INTERVALO_FRAMES = 2

CASCADE_PATH = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_alt2.xml")
if not os.path.exists(CASCADE_PATH):
    CASCADE_PATH = cv.data.haarcascades + "haarcascade_frontalface_alt2.xml"

face_cascade = cv.CascadeClassifier(CASCADE_PATH)
if face_cascade.empty():
    print("Error: No se pudo cargar el clasificador Haar Cascade.")
    sys.exit(1)


def main():
    print("=" * 60)
    print("  CAPTURA DE ROSTROS PARA DATASET (WEBCAM O VIDEO)")
    print("=" * 60)

    nombre_persona = input("Ingresa el nombre de la persona: ").strip()
    while not nombre_persona:
        nombre_persona = input("El nombre no puede estar vacío: ").strip()

    print("\nSelecciona el origen:")
    print(" [0] Cámara Web en vivo")
    print(" [1] Archivo de video")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        ruta_video = input("Ingresa la ruta completa o nombre del archivo de video: ").strip("\"' ")
        if not os.path.exists(ruta_video):
            print(f"Error: El archivo '{ruta_video}' no existe.")
            return
        fuente = ruta_video
    else:
        fuente = 0

    carpeta_persona = os.path.join(CARPETA_DATASET, nombre_persona)
    os.makedirs(carpeta_persona, exist_ok=True)

    fotos_existentes = [f for f in os.listdir(carpeta_persona) if f.lower().endswith(('.jpg', '.png'))]
    contador = len(fotos_existentes)

    cap = cv.VideoCapture(fuente)
    if not cap.isOpened():
        print(f"Error: No se pudo abrir la fuente de video: {fuente}")
        return

    print("\n" + "-" * 60)
    print(f"Directorio de guardado: {carpeta_persona}")
    print(f"Fotos previas encontradas: {contador}")
    print(f"Meta total: {CANTIDAD_FOTOS} fotos")
    print("Controles:")
    print("  - [ESPACIO]: Pausar / Reanudar captura")
    print("  - [ESC]: Salir y guardar progreso")
    print("-" * 60)

    frame_num = 0
    pausado = False

    while contador < CANTIDAD_FOTOS:
        if not pausado:
            ret, frame = cap.read()
            if not ret:
                print("\nℹ️ Fin del video o la cámara dejó de responder.")
                break
            frame_num += 1
        else:
            ret, frame = cap.read()
            if not ret:
                break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        rostros = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(60, 60)
        )

        for (x, y, w, h) in rostros:
            # 1. Recortamos y redimensionamos siempre para poder mostrar la ventanita
            rostro_roi = gray[y:y+h, x:x+w]
            rostro_resized = cv.resize(rostro_roi, TAMANO_ROSTRO, interpolation=cv.INTER_CUBIC)

            # 2. Solo guardamos en disco en los frames indicados por el intervalo
            if not pausado and (frame_num % INTERVALO_FRAMES == 0):
                archivo = os.path.join(carpeta_persona, f"rostro_{contador:04d}.jpg")
                cv.imwrite(archivo, rostro_resized)
                contador += 1

            # Dibujar en pantalla
            color = (0, 165, 255) if pausado else (0, 255, 0)
            cv.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv.putText(frame, f"{nombre_persona}: {contador}/{CANTIDAD_FOTOS}", (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.65, color, 2)

            # Mostrar la ventanita pequeña con el recorte
            cv.imshow("Recorte de Cara (100x100)", rostro_resized)

            if contador >= CANTIDAD_FOTOS:
                break

        if pausado:
            cv.putText(frame, "PAUSADO (Presiona ESPACIO para continuar)", (20, 40),
                       cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv.putText(frame, "Mueve la cabeza despacio y varia expresiones", (20, 30),
                       cv.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        cv.imshow("Captura de Rostros (Eigenfaces Dataset)", frame)

        tecla = cv.waitKey(1) & 0xFF
        if tecla == 27:  # ESC
            print("\nCaptura cancelada por el usuario.")
            break
        elif tecla == ord(' '):  # ESPACIO
            pausado = not pausado

    cap.release()
    cv.destroyAllWindows()

    print("=" * 60)
    print(f"✅ Finalizado para '{nombre_persona}'.")
    print(f"Total acumulado: {contador} fotos en {carpeta_persona}")
    print("=" * 60)


if __name__ == "__main__":
    main()

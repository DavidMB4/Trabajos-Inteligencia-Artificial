# Observaciones de reconocimiento facial con Eigenfaces, Fisherfaces y LBPH

**Dataset**: 5 clases (Aida, Farid, Juan, Karen, Vanessa) con 1,000 imágenes por persona a resolución 100×100 en escala de grises.

Para las pruebas utilicé mi cámara web. Puse un video de Farid Dieck en mi celular apuntando a la cámara para ver si lo reconocía, y también probé enfocando mi propia cara (la cual no está en las fotos de entrenamiento) para ver cómo reaccionaba cada modelo.

---

## 1. Eigenfaces

- **Con el video de Farid:** Le costó bastante trabajo reconocerlo. Casi todo el tiempo me marcaba "Desconocido" en rojo y solo en momentos muy específicos lo llegaba a reconocer como Farid.
- **Con mi cara:** En este caso funcionó bien el rechazo, ya que todo el tiempo me marcó como "Desconocido" y no me confundió con ninguno de los registrados.
- **Conclusión de este método:** Es muy sensible a la luz y al ángulo. Si la luz no es exactamente igual a la del video original, la distancia sube mucho y no reconoce a la persona.

---

## 2. Fisherfaces

- **Con el video de Farid:** Fue el que mejor lo reconoció, pero dependió mucho de la luz:
  - Cuando había mucha luz o le subía mucho el brillo al celular, por momentos se confundía y me ponía el nombre de otra persona en la pantalla.
  - Cuando le bajé el brillo al celular o había una luz más tenue, reconoció a Farid de forma clara y constante en verde.
- **Con mi cara:** Aquí tuvo un error (falso positivo), ya que al pararme yo frente a la cámara me reconoció por momentos como "Juan", a pesar de que no hay fotos mías en el dataset.
- **Conclusión de este método:** Es bueno reconociendo cuando la luz es adecuada, pero si hay exceso de brillo se confunde, y con personas que no están en el dataset tiende a buscar a quién se parece más en vez de marcarlo como desconocido.

---

## 3. LBPH

- **Con el video de Farid:** Con el umbral por defecto (70) casi no lo reconoció o lo detectaba muy pocas veces.
- **Con mi cara:** Al igual que Eigenfaces, a mí me marcó siempre como "Desconocido" sin confundirme.
- **Conclusión de este método:** Aunque en teoría aguanta mejor los cambios de luz, al mostrar la cara desde la pantalla de un celular frente a la webcam la textura de la imagen cambia un poco, por lo que casi no alcanzaba a pasar el umbral a menos que se ajuste para hacerlo más permisivo.

---

## Resumen general

- La luz afecta muchísimo el resultado en los tres métodos, demasiada luz hace que confundan a la gente, y poca luz hace que no los detecten.
- Fisherfaces fue el que más fácil reconoció a la persona conocida, aunque tuvo el problema de confundirme a mí con Juan.
- Eigenfaces y LBPH fueron más estrictos, por lo que no confundieron a gente desconocida, pero les costó más trabajo reconocer a la persona registrada a través de la pantalla.

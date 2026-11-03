━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXAMEN TEÓRICO — PERCEPTRÓN, MLP Y CNN (GRUPO B)

                            Eduardo Alcaraz
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1 Datos del alumno
══════════════════
━━━━━━━━━━━
David Maldonado Barajas  
 Fecha: 03/11/2026  
 ━━━━━━━━━━━

2 Pregunta 1 — Por qué no basta “una sola neurona”
══════════════════════════════════════════════════

1. Resume el funcionamiento de un perceptrón como “regla de decisión”.

2. Explica la noción de _frontera lineal_ sin escribir fórmulas.
   _Es una división que tiene forma de corte recto, para separar los datos en 2 grupos distintos_
3. Da un ejemplo (aunque sea inventado) donde esa frontera _no_
   alcanza.

2.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _Toma varias entradas, luego las multiplica cada una por un peso, sumas los resultados junto a un sesgo, y pasa el total por un umbral, si se pasa el umbral devuelve un 1, si no devuelve un 0_

    2. _Por ejemplo si en una feria, la regla para subir a un juego son niños entre 7 y 14 años, se tiene menos que 7 no suben y si tiene mas de 14 tampoco, con una sola linea no se puede aislar a los que estan en el medio de ese rango de edad._

└────

3 Pregunta 2 — CNN: de píxeles a mapas
══════════════════════════════════════

1. ¿Qué problema de _estructura espacial_ ignora un MLP si aplana la
   foto?

2. ¿Qué significa que un mismo filtro se aplique en toda la imagen?

3. Además de clasificación de objetos, cita _dos_ usos donde la CNN
   encaja bien.

3.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _Que se pierde la informacion de la imagen ya que quedan separados los pixeles y se pierde la forma que tenia._

    2. _Que se usa la misma plantilla para buscar la misma caracteristica en toda la imagen._

    3. _En la deteccion de objetos como la conducción autonoma en autos modernos, y la delimitacion de irregularidades en radiografias._

└────

4 Pregunta 3 — Softmax, clases y decisiones
═══════════════════════════════════════════

1. Diferencia un problema _binario_ de uno _multiclase_ en términos de
   salida de la red.

2. ¿Qué lectura le das a las probabilidades que produce un softmax?

3. Imagina tres carpetas de imágenes (tres riesgos o tres animales):
   ¿qué arquitectura de _salida_ usarías y por qué?

4.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _En la binario solo se tienen un neurona de salida que entrega un valor entre 0 y 1. mientras que en multiclase, la red tiene una neorona de salida por categoria, con las probabilidades suman 1._ 2. _Es distribucion de confianza que tiene el modelo sobre a que categoria pertence la entrada, garantiza que todos los valores sean positivos y sumen 100%._
└────

5 Pregunta 4 — MLP: profundidad con sentido
═══════════════════════════════════════════

1. ¿Qué ganas al apilar capas densas con activaciones no lineales?
2. ¿Qué riesgo aparece si la red es _demasiado_ grande para tus datos?
3. Relaciona “capa oculta” con la idea de aprender representaciones
   intermedias (en palabras simples).

5.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _Aprende las fronteras de desicion mas complejas, ayuda a resolver problemas que no son separables linealmente_

    2. _Puede aprender de forma general todo, lo que ele provoca un sobre ajuste donde puede fallar con datos nuevos._

    3. _Las capas ocultas actuán como procesadores intermedios que transforman los datos crudas, en algo mas util para poder tomar una decision final._

└────

6 Pregunta 5 — Entrenamiento sin magia
══════════════════════════════════════

1. Explica qué es una _época_ a nivel intuitivo.

2. ¿Hacia qué “objetivo” se mueven los pesos cuando hablamos de
   minimizar el error?
3. Si el learning rate es absurdo (muy grande o muy chico), ¿qué
   síntomas conceptuales esperarías?

6.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _Es una pasada completa en la que el modelo analiza y aprende de todo el conjunto de datos para entrenamiento una sola vez._

    2. _Se mueven hacia los valores que reducen lo mas posible la perdida, haciendo que las prediccion se acerquen los mas posible a algo real._

    3. _Si es muy chico avanza de forma muy lenta, y si es muy grande avanza de forma exagerada sin control provocando errores_

└────

7 Pregunta 6 — Bloques de una CNN
═════════════════════════════════

Sin matemáticas, di el papel de cada pieza:

1. Kernel / filtro convolucional
2. Función de activación después de conv
3. Max pooling
4. Capa densa + softmax al final de un clasificador

7.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌──── 1. _El kernel escanea la imagen buscando patrones visuales, como bordes, las esquinas, colores, etc._

    2. _La funcion de activacion permite resaltar solo donde se encontró algo importante mientras las demas zonas las apagada, ya que son zonas sin interes_

    3. _El Max pooling reduce el tamaño del mapa de caracteristicas, pero conserva solo el valor mas alto de cada zona para no perder lo mas importante._

    4. _Junta todas las caracteristicas extraidas, las conecta y calcula las probabilidades para asiganrle una clase a la imagen._

└────

8 Pregunta 7 — XOR y la historia del aprendizaje
════════════════════════════════════════════════

1. ¿Por qué XOR se volvió un “contraejemplo” famoso?
2. ¿Qué elemento de un MLP permite patrones que no son una sola línea?
3. ¿En qué tipo de tabla/problema del mundo real seguirías usando algo
   tan simple como un perceptrón o un modelo lineal?

8.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌────

└────

9 Pregunta 8 — De lo simple a lo abstracto en visión
════════════════════════════════════════════════════

1. Contrasta lo que buscan capas tempranas vs capas profundas en una
   CNN.
2. ¿Qué intuición da eso para _transfer learning_ (aunque no lo hayas
   programado)?
3. ¿Cuándo sospecharías que tu CNN es “profunda de más” para el
   dataset del curso?

9.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌────

└────

10 Pregunta 9 — Análisis: matching problema → modelo
════════════════════════════════════════════════════

Elige _Perceptrón/lineal_ / _MLP_ / _CNN_ (una opción) y justifica en
una frase:

1. Predecir “compra / no compra” con edad, ingreso y visitas a la web
   (columnas numéricas).
2. Detectar si hay un gato en una foto.
3. Aproximar una frontera “curva” o a trozos en datos 2D tabulares.
4. ¿CNN es la herramienta natural para predecir la siguiente palabra
   de un párrafo? Justifica y nombra una familia del curso más
   adecuada (RNN/Transformer a nivel nombre).

   10.0.1 Respuesta
   ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌────

└────

11 Pregunta 10 — Análisis: auditoría de un equipo
═════════════════════════════════════════════════

Un equipo entrega un modelo “muy preciso” en su laptop y falla con
datos nuevos.

1. ¿Qué diagnósticos conceptuales harías _antes_ de tocar
   hiperparámetros al azar?
2. Pide _dos_ evidencias que deberían mostrar en la defensa (curvas,
   separación train/val, ejemplos de error, etc.).
3. Redacta _tres_ preguntas tuyas para comprobar si saben cuándo usar
   perceptrón, MLP o CNN (distintas a las del Grupo A si las conoces).

   11.0.1 Respuesta
   ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

┌────

└────

## Comparativa de modelos en el caso de auditoría "El filtro milagroso"

Se utilizó exactamente el mismo documento (el de los filtros) de pistas y el mismo prompt en modo Consulta dentro de AnythingLLM para evaluar cómo responde cada modelo local ante un caso con información fragmentada.

### Tabla comparativa de comportamiento

| Aspecto comparado                   | `deepseek-r1:8b`                                                                                                                   | `llama3.2:3b`                                                                                                    | `qwen2.5-coder:7b`                                                                                        |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Tiempo y velocidad**              | Fue el más lento, tardó más de 6 minutos porque se detiene a "pensar" paso a paso antes de contestar.                              | Rápido, respondió casi de inmediato al ser el más ligero.                                                        | Fue el intermedio, noo tarda tanto como DeepSeek.                                                         |
| **Cómo ordenó la respuesta**        | Texto largo dividido por sobres y preguntas, con mucha explicación.                                                                | Siguió el orden de los sobres y las preguntas del documento de forma directa.                                    | Usó tablas para mostrar supuestos cálculos y dividió por secciones.                                       |
| **¿Identificó los nombres reales?** | No, no mencionó a ninguno de los participantes reales (Mirna, Elsa, Hugo, Leo, Óscar, Julia); habló de "grupos" o del "encargado". | No, tampoco dio nombres propios; dijo cosas genéricas como "el miembro del equipo" o "el juez".                  | No, usó etiquetas genéricas como "el investigador" y aclaró que no se podía asegurar el nombre.           |
| **¿Qué inventó o alucinó?**         | Inventó códigos de muestra que no existen (`ID 145`, `ID 146`) y horas falsas (`14:00`), asegurando que hubo fraude deliberado.    | Inventó porcentajes distintos, una hora falsa (`14:15`) y dijo que el ganador real seguía siendo el Filtro Azul. | Inventó una tabla entera de porcentajes y códigos genéricos (`ID_123`, `ID_456`) que no vienen en el PDF. |
| **Conclusión a la que llegó**       | Culpa a quien supervisó y validó el boletín durante la sesión compartida de las 14:00.                                             | Culpa al integrante que manejó la sesión compartida y dice que el juez lo aprobó.                                | Culpa a un investigador anónimo que lavó mal la muestra y aprobó los datos falsos.                        |

---

### Diferencias entre las repuestas de los 3

1. Ninguno logró dar con los nombres reales del caso, aunque el documento sí dice quiénes participaron y qué hizo cada uno, los tres modelos no lograron cruzar las pistas en modo Consulta y usaron frases genéricas en lugar de nombres propios.
2. Cada uno rellenó los huecos a su manera, por ejemplo:
   - **`deepseek-r1:8b`** intentó sonar muy analítico y detallado, pero terminó inventando números de identificación como `145`, `146` y horarios como `14:00` para justificar una historia de fraude.
   - **`llama3.2:3b`** fue el más directo, pero confundió los resultados reales, porque dijo que ganaba el Azul con las pruebas válidas, cuando en realidad ganaba el Verde y también inventó horarios como el de `14:15`.
   - **`qwen2.5-coder:7b`** se fue por el lado visual haciendo tablas de números, pero todos los datos dentro de sus tablas y códigos fueron inventados como los ID `ID_123`, `ID_456`.
3. `deepseek-r1:8b` tarda muchísimo más en responder porque razona antes de escribir, mientras que `llama3.2:3b` y `qwen2.5-coder:7b` contestan rápido, pero los tres sufren cuando tienen que unir muchas pistas sueltas de un PDF.

---

### Respuestas obtenidas por cada modelo

#### 1. Respuesta de `deepseek-r1:8b`

````Análisis del Filtro Milagroso

Sobre 1:

Posibles ganadores iniciales: El boletín inicial menciona un “filtro milagroso” con resultados destacados, pero no proporciona los datos específicos de cada prueba. Solo sabemos que el resultado publicado es altísimo (91%).
Datos en el boletín: La hoja de trabajo inicial (Sobre 1) contiene datos en el boletín pero no menciona claramente los IDs de las muestras. Solo la conclusión final debería haberlo hecho.
Qué aún debe verificarse (Sobre 1):
El 91%: ¿Es un dato real o es el resultado de una sustitución? El boletín inicial no lo aclara.
Los IDs de las muestras: ¿Están correctos en las tablas de resultados? El Sobre 1 solo enumera los IDs sin verificarlos.
La hora: El Sobre 1 menciona la hora oficial para todos los eventos, pero no se proporciona información sobre la hora del evento o el ID del grupo.
Sobre 2:

Contraste de IDs: En la hoja de trabajo (Sobre 1), los resultados muestran IDs que no coinciden con los IDs originales de las muestras (como el ID 145). Esto indica una sustitución.
Diferencia entre versiones: Hay una versión inicial del boletín (probablemente la que se muestra en el Sobre 1) y una versión corregida (Sobre 3). Los datos en el Sobre 1 son sospechosos.
Sesión compartida: La evidencia de la sesión compartida (hora oficial) muestra que los eventos no ocurrieron en el mismo momento, lo que contradice la posibilidad de un solo grupo realizando todas las acciones de manera simultánea. Esto apoya la idea de que diferentes grupos o personas realizaron acciones separadas.
Sobre 3:

Dictamen corregido: El Sobre 3 contiene la hoja de análisis 2 (cronología y dictamen) donde se reescribe la historia cronológica con la hora oficial. Esto es crucial para entender la línea de tiempo de los eventos.
Atribución proporcional: No se proporciona una atribución clara, pero los diferentes IDs y las diferentes horas de los eventos sugieren que varias personas o grupos estuvieron involucrados en la sustitución, la edición y la defensa.
Preguntas del dictamen contestadas:

Rendimiento de cada ensayo y promedio de cada filtro:

Filtro Azul (Ganador): Los datos originales (IDs válidos) de las tablas muestran resultados muy bajos para las pruebas realizadas con muestras originales (por ejemplo, ID 145 muestra un azul bajo en todas las pruebas). El promedio de estos ensayos es bajo.
Filtro Control: El rendimiento del control (ID 146) es consistente (por ejemplo, valores de 0.5, 0.7, etc.) y su promedio es bajo.
El 91%: Este resultado proviene de ensayos con muestras incorrectas (IDs alterados). Las tablas muestran valores muy altos (91%) pero con IDs que no existen en las muestras originales (como ID 145).
Filtro que habría ganado con las 12 pruebas válidas:

Si se realizan 12 pruebas válidas con las muestras originales (IDs 145, 146, etc.), el rendimiento probablemente sería el de los filtros originales (Control y Azul) o similar, que es bajo. El 91% es resultado de ensayos fraudulenteros con muestras no originales.
Cómo se obtuvo 91% con cifras reales pero muestras incorrectas:

Los cálculos validan que los valores numéricos de eliminación de colorante en las tablas (los que dan 91%) son consistentes entre sí, lo que sugiere que son datos reales. Sin embargo, estos valores altos no corresponden a las muestras originales (IDs válidos) que se enumeran en las mismas tablas o en el boletín. Esos mismos datos reales provienen de muestras con IDs diferentes (como ID 145), que no existen. Por lo tanto, se mezcló el ID de las muestras originales (bajas) con el ID de las muestras reales pero incorrectas (altas).
Corrección de los sellos de hora y reconstrucción del boletín:

Los sellos de hora originales en el boletín son sospechosos (por ejemplo, dos eventos a las 14:00). La hora oficial de los eventos (reconstruida en Sobre 3) muestra una secuencia cronológica lógica, con eventos realizados en momentos distintos por diferentes grupos.
Quién efectuó la sustitución, quién la aprobó y quién se benefició:

Quién efectuó la sustitución: Los grupos que realizaron las pruebas y reportaron los IDs alterados (como ID 145) son los sospechosos directos. El hecho de que diferentes IDs tengan la misma hora de edición (14:00) sugiere que varios grupos (o al menos dos) participaron en la sustitución durante la misma sesión compartida (14:00).
Quién la aprobó: El responsable de la sesión compartida (probablemente el profesor o el encargado del concurso) que permitió el uso del mismo reloj y la edición conjunta, y validó las tablas antes de publicarlas, es el responsable de aprobar el fraude.
Quién se benefició: El equipo que utilizó el ID 145 (y posiblemente otros IDs alterados) para obtener un resultado de 91% en sus cálculos, lo que les permitió clasificarse como ganadores en la primera ronda.
Conclusión sobre el caso:

El caso del “filtro milagroso Azul” fue el resultado de un fraude deliberado. Los datos reales de los ensayos originales (probablemente con el filtro Control) mostraban un rendimiento bajo, pero se sustituyeron los IDs de las muestras en las tablas de resultados para hacerlos coincidir con datos de eliminación de colorante altos (91%). Esta sustitución ocurrió durante una sesión compartida (probablemente a las 14:00), donde diferentes grupos (identificados por diferentes IDs) se beneficiaron de los mismos datos reales alterados para obtener resultados falsamente altos. El responsable de la sesión compartida validó los datos alterados, permitiendo que el equipo con el ID 145 (y posiblemente otros) se presentara como el ganador basado en resultados que no eran ni consistentes con las muestras originales ni posiblemente reales.

El responsable fue la persona que supervisó y validó el sistema de puntuación durante la sesión compartida (a las 14:00), sin cuestionar la coherencia y autenticidad de los datos. El encargado de revisar y autorizar la actualización del boletín fue el responsable final de la filtración y el fraude deliberado en el informe.```

#### 2. Respuesta de `llama3.2:3b`

```Con base en el documento proporcionado, realizaré las actividades solicitadas.

Sobre 1: Calculen tres posibles ganadores a partir de los datos disponibles y detecten qué aún debe verificarse.

Después de analizar los resultados, puedo identificar los siguientes tres posibles ganadores:

Filtro Azul con un 91% de eliminación de colorante.
Filtro Verde con un 85% de eliminación de colorante.
Filtro Rojo con un 78% de eliminación de colorante.
Sin embargo, aún debo verificar la calidad de las muestras y los datos para determinar si estos resultados son confiables.

Sobre 2: Contrasten IDs de ensayo y lavado, las dos versiones y la sesión compartida.

Después de analizar los datos, puedo identificar los siguientes problemas:

El ID de la prueba 1 es válido, pero el ID de la prueba 2 es válido solo para el filtro Verde.
La versión 1 del boletín tiene un ID válido, pero la versión 2 tiene un ID inválido.
La sesión compartida tiene un ID inválido.
Estos problemas sugieren que hay una sustitución de datos, pero no puedo determinar quién fue el responsable sin más información.

Sobre 3: Construyan el informe corregido y una atribución proporcional a las pruebas.

Después de analizar los datos y realizar los cálculos necesarios, puedo presentar el informe corregido y la atribución proporcional a las pruebas:

Filtro Azul: 60% de la puntuación total (91% de eliminación de colorante en la prueba 1, pero 85% en la prueba 2)
Filtro Verde: 30% de la puntuación total (85% de eliminación de colorante en la prueba 2)
Filtro Rojo: 10% de la puntuación total (78% de eliminación de colorante en la prueba 3)
Preguntas que su dictamen debe contestar

Calculen el rendimiento de cada ensayo y el promedio de cada filtro.
Después de realizar los cálculos, puedo presentar los rendimientos de cada ensayo y el promedio de cada filtro:

Filtro Azul: promedio de 87,5%
Filtro Verde: promedio de 82,5%
Filtro Rojo: promedio de 75%
¿Qué filtro habría ganado con las 12 pruebas válidas?
Después de analizar los datos, puedo determinar que el Filtro Azul habría ganado con las 12 pruebas válidas.

¿Cómo se obtuvo 91% con cifras reales pero muestras incorrectas?
La sustitución de datos es la razón por la que se obtuvo un 91% con cifras reales pero muestras incorrectas.

Corrijan los sellos de hora y reconstruyan la actualización del boletín.
Después de analizar los sellos de hora, puedo corregir los errores y reconstruir la actualización del boletín:

Hora original: 14:00
Corrección: 14:15
Actualización del boletín: “Se actualizó el boletín a las 14:15 con la información actualizada”
¿Quién efectuó la sustitución, quién la aprobó y quién se benefició?
Después de analizar los datos, puedo determinar que:

El sustitutor fue el miembro del equipo que se encargó de la sesión compartida.
El aprobador fue el juez de la feria científica.
El beneficiario fue el equipo del Filtro Azul, ya que su puntuación se vio afectada por la sustitución de datos.
Conclusión

En conclusión, se encontró que el Filtro Azul ganó con un 91% de eliminación de colorante, pero debido a la sustitución de datos, sus resultados se vieron afectados. La sustitución de datos fue realizada por el miembro del equipo que se encargó de la sesión compartida, y fue aprobada por el juez de la feria científica. El equipo del Filtro Azul se benefició de la sustitución de datos, ya que su puntuación se vio afectada.

La auditoría concluyó que es necesario realizar una mayor verificación de los datos y asegurarse de que se sigan las normas de calidad en las ferias científicas.```

#### 3. Respuesta de `qwen2.5-coder:7b`

```Sobre 1: Calcula tres posibles ganadores a partir de los datos disponibles y detecta qué aún debe verificarse.

Calculo del rendimiento de cada ensayo y el promedio de cada filtro:
FILTRO PRUEBA 1 PRUEBA 2 PRUEBA 3 PRUEBA 4 PROMEDIO
Control de origen de las muestras 85 80 90 75 84
Filtro Azul 95 85 92 88 90
Filtro Rojo 70 65 75 72 71
Filtro Verde 90 88 93 86 89
Promedio del Control de origen de las muestras: 84% Promedio del Filtro Azul: 90% Promedio del Filtro Rojo: 71% Promedio del Filtro Verde: 89%

El Filtro Azul tiene el mayor rendimiento con un promedio del 90%.

Sobre 2: Contrasten IDs de ensayo y lavado, las dos versiones y la sesión compartida.

ID de ensayo y lavado:

ID_123: Ensayo original - Lavado incorrecto
ID_456: Ensayo correcto - Lavado correcto
Dos versiones:

Versión A: Datos reales - Resultados correctos
Versión B: Datos falsificados - Resultados incorrectos
Sesión compartida:

Todos los ensayos y lavados fueron realizados en una sesión compartida.
Sobre 3: Construye el informe corregido y una atribución proporcional a las pruebas.

Informe Corregido:

FILTRO PRUEBA 1 PRUEBA 2 PRUEBA 3 PRUEBA 4 PROMEDIO
Control de origen de las muestras 85 80 90 75 84
Filtro Azul 95 85 92 88 90
Filtro Rojo 70 65 75 72 71
Filtro Verde 90 88 93 86 89
Dictamen del Equipo:

Qué ocurrió (hecho comprobable): La muestra de ID_123, que era el control de origen de las muestras, fue lavada incorrectamente, lo que afectó su resultado. El Filtro Azul obtuvo el 91% anunciado debido a esta falsificación.

Quién hizo qué (separar acciones y personas):

El investigador que realizó el lavado incorrectamente fue el responsable de la sustitución.
El investigador que aprobó los resultados falsificados fue el responsable de la aprobación.
El investigador que se benefició de los resultados falsificados fue el que obtuvo una posición en el concurso.
Evidencias principales (IDs de tarjetas y cálculos):

ID_123
ID_456
Lo que aún no puede asegurarse: El nombre del investigador que realizó la sustitución, aprobó los resultados y se benefició del mismo.

Conclusión: El responsable del fraude fue el investigador que realizó la sustitución de las muestras y aprobó los resultados falsificados, con el fin de obtener una posición en el concurso.```
````

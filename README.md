# Tesoro Literario
¡Por supuesto! 🙌
Aquí tienes una **explicación clara y resumida** sobre cómo se realizó el juego y cómo se juega, ideal para presentarlo o incluirlo en tu informe del proyecto.

---

## 🧩 **Juego: "Descubriendo Ciudades"**

### 🎯 **Objetivo del juego**

El jugador debe recorrer las principales **ciudades de Colombia**, respondiendo correctamente **preguntas de lengua castellana** (sinónimos, antónimos, sustantivos, verbos, etc.).
Cada respuesta correcta **desbloquea la siguiente ciudad**, hasta completar el recorrido por todo el país.

---

## 💻 **Cómo se realizó el juego**

1. **Lenguaje utilizado:**
   Se desarrolló en **Python** usando el **framework Flask**, que permite convertir programas de consola en **aplicaciones web interactivas**.

2. **Estructura general del código:**

   * En el archivo `main.py` se define:

     * El **temario** (lista de preguntas, opciones y respuestas).
     * Las **rutas** de Flask (`/`, `/pregunta/<nivel>`, `/fin`), que indican qué página debe mostrar el servidor en cada momento.
     * La **lógica del juego**: si la respuesta del jugador es correcta, avanza; si no, puede intentar de nuevo.
   * En la carpeta **`templates`** se guardan las **páginas HTML**:

     * `index.html`: pantalla de inicio con el botón “Comenzar juego”.
     * `pregunta.html`: muestra cada pregunta y botones para elegir una respuesta.
     * (opcional) `fin.html`: mensaje final de felicitación.

3. **Funcionamiento técnico:**

   * Flask ejecuta un **servidor web local** que envía las páginas HTML al navegador.
   * Cada vez que el jugador selecciona una respuesta, se envía esa elección al servidor.
   * El servidor compara la respuesta con la correcta y decide si avanzar al siguiente nivel o mostrar un mensaje de error.

4. **Ejecución en Replit:**

   * Se presiona **▶️ Run** para iniciar el servidor Flask.
   * Replit genera un enlace del tipo:
     `https://descubriendociudades-angelapsuarez.replit.app`
   * Ese enlace abre el juego en el navegador como una **aplicación web jugable**.

---

## 🎮 **Cómo se juega**

1. Abre el enlace del juego en tu navegador.
2. En la pantalla de inicio, haz clic en **“Comenzar juego”**.
3. Aparecerá la primera ciudad (Bogotá) con una pregunta.
4. Haz clic en la opción que creas correcta.

   * Si aciertas, el juego te lleva automáticamente a la siguiente ciudad.
   * Si fallas, aparece el mensaje “❌ Respuesta incorrecta. Intenta de nuevo.”
5. Al llegar al último nivel (Cúcuta), el juego muestra un mensaje de **felicitación** por haber completado el recorrido.

---

## 🌟 **Resumen general**

| Aspecto              | Descripción                                                        |
| -------------------- | ------------------------------------------------------------------ |
| **Nombre del juego** | Descubriendo Ciudades                                              |
| **Tipo**             | Juego educativo interactivo                                        |
| **Lenguaje**         | Python (Flask) + HTML/CSS                                          |
| **Tema**             | Lengua castellana y cultura colombiana                             |
| **Modo de juego**    | Preguntas de opción múltiple por niveles                           |
| **Objetivo final**   | Completar el recorrido por las ciudades respondiendo correctamente |

---

¿Quieres que te prepare una **versión breve (1 párrafo)** para colocar en la descripción del proyecto en Replit o un **texto formal para informe escolar** (una página corta)?

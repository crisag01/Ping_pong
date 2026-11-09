🏓 Ping Pong (Python)
Juego de ping pong para dos jugadores en la misma computadora, hecho con Python en 2023. Lo programé para practicar la creación de interfaces gráficas, el manejo del teclado y la lógica de un juego en tiempo real.

Antes de empezar, el juego pide el nombre de cada jugador y lo muestra en el marcador.

🎮 Cómo se juega
Al iniciar, escribe el nombre del Jugador 1 y del Jugador 2.
Se abre la cancha: una paleta a cada lado y la pelota en el centro.
Cada jugador mueve su paleta para regresar la pelota.
Si la pelota pasa la paleta de tu rival, ganas un punto y la pelota vuelve al centro hacia el otro lado.
El marcador de arriba muestra los puntos de cada jugador con su nombre.

⌨️ Controles
Jugador	Subir	Bajar
Jugador 1 (izquierda)	W	S
Jugador 2 (derecha)	↑	↓


▶️ Cómo ejecutarlo
Solo necesitas Python 3. Usa turtle y tkinter, que vienen incluidos con Python, así que no hay que instalar librerías.

git clone https://github.com/crisag01/Ping_pong.git
cd Ping_pong
python3 ping_pong.py
Si usas Python instalado con Homebrew en Mac y aparece un error de tkinter, instálalo con brew install python-tk.

🧠 Qué practiqué
Módulo turtle                       ---  Dibujar la cancha, las paletas, la pelota y el marcador
tkinter y simpledialog	            ---  Ventana de bienvenida que pide el nombre de los jugadores
Eventos de teclado                 	---  onkeypress para mover cada paleta con sus teclas
Funciones	                          ---  Una función para subir y otra para bajar cada paleta
Ciclo principal (while True)	      ---  Actualizar la pantalla y mover la pelota en cada cuadro
Coordenadas y velocidad	            ---  dx y dy para el movimiento de la pelota
Detección de colisiones             ---  Rebote en los bordes y choque con las paletas
Contadores y texto con formato	    ---  Llevar y mostrar el puntaje con format()


👤 Autor
Cristian Armenta, ingeniero industrial y analista de datos. Más proyectos en crisag.com.

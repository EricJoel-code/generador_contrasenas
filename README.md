
🎉 Generador de Contraseñas con Interfaz Gráfica 🎉
¡Bienvenido al Generador de Contraseñas! Este proyecto te permite generar contraseñas seguras con varias opciones de personalización a través de una interfaz gráfica amigable desarrollada con Tkinter. 🔐


🚀 Características
Generación de contraseñas a medida:

🔡 Solo minúsculas.
🔠 Solo mayúsculas.
🔢 Solo números.
📄 Basada en un texto de referencia.
🔡🔠 Combinación de letras mayúsculas y minúsculas.
🔣 Mezcla personalizada de letras, números y símbolos.
🔀 Mezcla de todos los caracteres posibles.
📝 Generación de contraseñas a partir de un texto proporcionado por el usuario.
Funcionalidad avanzada:

💾 Guardar la contraseña generada en un archivo de texto (contraseñas.txt).
🔄 Opción para regenerar una nueva contraseña con un solo clic.
🧹 Limpiar los campos automáticamente para una nueva generación.
🛠️ Requisitos
Python 3.x (descárgalo desde python.org)
Tkinter (incluido con Python por defecto)
🗂️ Estructura del Proyecto
bash
Copiar código
password_generator/
│
├── password_generator.py   # Lógica de generación de contraseñas
├── main.py                 # Interfaz gráfica de usuario con Tkinter
└── README.md               # Documentación del proyecto
📦 Instalación
Clona el repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/EricJoel-code/generador_contrasenas.git
Navega hasta el directorio del proyecto:

bash
Copiar código
cd generador-contrasenas
Asegúrate de tener Python 3.x instalado. Si no lo tienes, descárgalo desde python.org.

💻 Uso
Ejecuta el archivo main.py para iniciar la interfaz gráfica:

bash
Copiar código
python main.py
En la ventana de la aplicación, selecciona el tipo de contraseña que deseas generar:

Puedes elegir entre letras minúsculas, mayúsculas, números, o una combinación.
Si eliges "Con referencia", proporciona un texto que servirá como base de la contraseña.
Ingresa la longitud de la contraseña y presiona el botón Generar.

La contraseña aparecerá en pantalla y tendrás la opción de guardar la contraseña generada en un archivo de texto (contraseñas.txt).

Si deseas crear otra contraseña, haz clic en Generar otra contraseña para limpiar los campos y reiniciar el proceso.

📝 Ejemplo de Uso
Imagina que quieres generar una contraseña basada en el texto de referencia "HolaMundo" con una combinación de letras y números. Así es como podría verse:

text
Copiar código
La contraseña generada es: H0laMund0!#
🌟 Personalización
Este generador es completamente personalizable. Si deseas cambiar las reglas de generación, simplemente edita el archivo password_generator.py. Por ejemplo, puedes ajustar las reglas de sustitución de caracteres para las referencias en la función transformar_texto_a_contraseña.

🤝 Contribuciones
¡Contribuciones, ideas y mejoras son siempre bienvenidas! Si encuentras un error o tienes una sugerencia, abre un issue o envía un pull request.


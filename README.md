Generador de Contraseñas con Interfaz Gráfica
Este es un proyecto en Python que permite generar contraseñas seguras de diferentes tipos mediante una interfaz gráfica desarrollada con Tkinter. El generador incluye opciones para generar contraseñas de solo minúsculas, mayúsculas, números, o incluso basadas en un texto de referencia. Las contraseñas generadas también se pueden guardar en un archivo.

Características
Opciones de generación:
Solo minúsculas.
Solo mayúsculas.
Solo números.
Con una referencia específica.
Mezcla de letras (mayúsculas y minúsculas) con referencia.
Personalizada (letras, símbolos, y/o números).
Mezcla de todos los caracteres.
A partir de un texto proporcionado.
Guardar contraseñas: Posibilidad de guardar las contraseñas generadas en un archivo de texto (contraseñas.txt).
Generar nuevamente: Opción para generar otra contraseña y limpiar los campos.
Requisitos
Python 3.x
Tkinter (incluido por defecto en la instalación de Python)
Estructura del Proyecto
bash
Copiar código
password_generator/  
│
├── password_generator.py   # Lógica de generación y almacenamiento de contraseñas
├── main.py                 # Interfaz gráfica con Tkinter
└── README.md               # Archivo README
Instalación
Clona o descarga este repositorio en tu máquina local.

bash
Copiar código
git clone https://github.com/EricJoel-code/generador_contrasenas.git
Navega hasta el directorio del proyecto.

bash
Copiar código
cd generador-contrasenas
Asegúrate de tener Python 3.x instalado. Si no lo tienes, puedes descargarlo desde python.org.

Uso
Ejecuta el archivo main.py para iniciar la interfaz gráfica del generador de contraseñas.

bash
Copiar código
python main.py
En la interfaz gráfica, selecciona el tipo de contraseña que deseas generar.

Si seleccionas la opción "Con referencia", ingresa un texto que será usado como base para la contraseña.
Para opciones avanzadas, puedes elegir incluir símbolos o números.
Ingresa la longitud de la contraseña (si aplica) y presiona el botón Generar.

La contraseña se mostrará en pantalla y, si seleccionaste la opción, también se guardará en un archivo contraseñas.txt.

Si deseas generar otra contraseña, presiona el botón Generar otra contraseña para limpiar los campos y empezar de nuevo.

Ejemplo
Ejemplo de una contraseña generada a partir del texto "holaMundo" con caracteres especiales añadidos:

graphql
Copiar código
La contraseña generada es: h0l@Mund0!#
Personalización
Puedes personalizar la lógica de generación de contraseñas editando el archivo password_generator.py. Las reglas de sustitución de caracteres en las referencias se pueden ajustar en la función transformar_texto_a_contraseña.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una sugerencia de mejora, no dudes en abrir un issue o enviar un pull request.
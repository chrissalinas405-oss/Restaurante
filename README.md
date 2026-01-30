🍽️ KCB Restaurant App
Una aplicación móvil construida con Python y Kivy, diseñada para visualizar menús de restaurantes de forma dinámica mediante la lectura de archivos de datos estructurados.

📝 Descripción
La aplicación permite a los usuarios navegar por las categorías de un restaurante (Entradas, Platos Fuertes, Bebidas, etc.) y visualizar los detalles de cada producto.

Características principales:
Carga Dinámica: El menú se genera automáticamente a partir de un archivo menu.json.

Interfaz Adaptativa: Diseño optimizado para dispositivos móviles con una estética elegante en tonos oscuros y dorados.

Gestión de Estados: Navegación fluida entre pantallas (Inicio, Categorías y Productos).

Generación de Recursos: Si el logo o el menú no existen, la app los crea automáticamente para asegurar su funcionamiento inicial.

🚀 Cómo ejecutar la aplicación
Sigue estos pasos para configurar el entorno y correr el proyecto en tu computadora:

1. Requisitos previos
Asegúrate de tener instalado Python 3.x en tu sistema.

2. Instalación de dependencias
Necesitarás instalar Kivy (el framework de la interfaz) y Pillow (para la generación automática del logo). Abre tu terminal y ejecuta:

Bash
pip install kivy pillow
3. Preparación de archivos
Asegúrate de tener en la misma carpeta:

main.py (el código que pegaste arriba).

menu.json (el archivo con la lista de productos). Si no lo tienes, la app creará uno de ejemplo al iniciar.

4. Ejecución
Para iniciar la aplicación, simplemente corre el script principal:

Bash
python main.py
🛠️ Tecnologías utilizadas
Python: Lógica de programación.

Kivy & KV Language: Diseño de la interfaz de usuario y manejo de eventos.

JSON: Almacenamiento y estructuración de los datos del menú.

PIL (Pillow): Procesamiento de imágenes para el branding de la app.


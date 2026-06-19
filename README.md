# Urban Grocers - Automated Testing Suite 🛒🍔

**Urban Grocers** es una API de servicios de delivery que conecta a los usuarios con diferentes restaurantes de la ciudad.

En este sprint, el objetivo principal es validar el flujo del backend que permite el registro de nuevos usuarios y la posterior personalización de sus perfiles. Una vez que un usuario se registra de forma exitosa, la API genera de manera automática un **token de autenticación único (`authToken`)**. Con esta llave de acceso temporal, el usuario queda completamente habilitado para crear y configurar su propio **kit de productos**.

Esta suite de pruebas automatizadas se encarga de auditar la estabilidad de estos endpoints, enfocándose de manera estricta en la lógica de límites para la función de asignación de nombres a los kits de los clientes.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** Python 3.14+
* **Framework de Pruebas:** Pytest 9.0.3
* **Librería HTTP:** Requests (para la estructuración y consumo de peticiones REST)
* **IDE:** PyCharm

---

## 📂 Estructura Real del Proyecto

De acuerdo con la arquitectura actual de nuestro repositorio, los módulos se dividen de la siguiente manera:

* `configuration.py`: Almacena la URL base del servidor simulado y las rutas absolutas (`endpoints`) de la API.
* `data.py`: Contiene los diccionarios base con los cuerpos de las solicitudes (`user_body`, `kit_body`) y los encabezados de red (`headers`).
* `sender_stand_request.py`: Aloja las funciones lógicas que estructuran y disparan las peticiones HTTP (`GET`, `POST`) utilizando métodos de la librería `requests`.
* `create_kit_name_kit_test.py`: Suite de pruebas unitarias y de integración encargada de ejecutar los escenarios de prueba sobre la creación del nombre de los kits.
* `main.py`: Archivo de ejecución secundario o de pruebas rápidas del entorno.

---

## ⚙️ Configuración del Entorno de Desarrollo

Para ejecutar estas pruebas localmente y asegurar la compatibilidad de las librerías, ejecuta los siguientes comandos desde la terminal integrada de PyCharm:

1. **Activar el entorno virtual local:**
   ```bash
   # En Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   #Instalar las dependencias del proyecto:
    Bash
    pip install pytest requests

   #Sincronizar la dirección del servidor simulado:
    Antes de lanzar las pruebas, abre el archivo configuration.py y asegúrate de actualizar la variable URL_SERVICE con la dirección web activa que te proporcione el simulador de la plataforma de Urban Grocers.
___


## 🧪 Ejecución de las Pruebas

Para lanzar la suite de pruebas completa y observar las impresiones de depuración en tiempo real, ejecuta el siguiente comando en tu consola:

    #pytest create_kit_name_kit_test.py -v -s
 (El flag -v incrementa la verbosidad del reporte final detallando el estado de cada test, y el flag -s desactiva la captura de salida para permitirnos ver los mensajes de logs internos e impresiones de variables como los tokens o tablas).

___

## 🎯 Casos de Prueba Cubiertos & Estrategia de QA

Los escenarios automatizados en create_kit_name_kit_test.py se diseñaron aplicando técnicas de Análisis de Valores Límite (BVA) y Partición de Equivalencia directamente sobre la función de creación del nombre del kit:

___

## 📦 Pruebas de Límites en "Crear nombre del kit"
* *Casos Positivos* (201 Created / 200 OK):

Validación de la longitud mínima permitida para el nombre del kit (1 carácter).

Validación de la longitud máxima permitida (Límite superior exacto del sistema).

Uso de caracteres alfanuméricos, espacios intermedios y caracteres especiales permitidos por las reglas del negocio.

* *Casos Negativos* (400 Bad Request):

Envío de un nombre de kit completamente vacío (longitud 0).

Superación del límite máximo de caracteres permitidos para comprobar que el sistema bloquea solicitudes desbordadas.

Inyección de tipos de datos incorrectos en el parámetro del nombre.

___

## 🔑 Gestión Dinámica de Autenticación

Cada caso de prueba es completamente independiente. Los tests llaman internamente a las funciones de creación de usuario para extraer un authToken único en tiempo de ejecución.

Para evitar efectos secundarios o la contaminación de datos entre pruebas concurrentes, el código clona los diccionarios de configuración (data.kit_body.copy()) modificando únicamente los parámetros locales necesarios para cada aserción.

___
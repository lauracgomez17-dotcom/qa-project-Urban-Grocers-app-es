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
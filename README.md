# Pipeline de Despliegue en AWS EC2

Este proyecto incluye un pipeline automatizado para desplegar una aplicación en una instancia EC2 de AWS. A continuación, se detalla la configuración y los pasos necesarios para realizar el despliegue.

## Configuración del Pipeline

El pipeline está configurado para ejecutarse cada vez que se realiza un `push` en la rama principal (`main`). Se realiza en un entorno Ubuntu y contiene los siguientes pasos:

### Pasos del Pipeline

1. **Checkout del código**: Obtiene el código del repositorio actual para su despliegue.
2. **Configuración de la clave SSH**: Configura la clave SSH para permitir la conexión segura con la instancia EC2.
3. **Instalación de dependencias en la instancia EC2**: Se actualiza el sistema operativo y se instalan las dependencias necesarias, como Python y Git.
4. **Clonación o actualización del repositorio**: Clona el repositorio en la instancia EC2 si no existe; si ya está clonado, actualiza el código.
5. **Creación del entorno virtual**: Configura un entorno virtual de Python y se instalan las dependencias listadas en `requirements.txt`.
6. **Creación del archivo `.env`**: Configura las credenciales necesarias, como la URI de MongoDB, en un archivo de entorno.
7. **Reinicio de la aplicación**: Activa el entorno virtual y ejecuta la aplicación en segundo plano, redirigiendo los logs a un archivo.
8. **Validación del despliegue**: Verifica que la aplicación esté funcionando correctamente mediante una solicitud `curl` al endpoint principal.

---

## Descripción de la Aplicación

La aplicación es una API que ofrece dos endpoints principales para gestionar tareas. 

### Endpoints

1. **GET `/listar_tareas`**
   - Descripción: Este endpoint devuelve una lista de todas las tareas almacenadas en la base de datos eliminando la id asociada a cada tarea.
   - Ejemplo de respuesta:
     ```json
     [
       {
         "titulo": "Comprar leche",
         "descripcion": "Ir al supermercado y comprar leche",
         "estado": "pendiente"
       },
       {
         "titulo": "Llamar amigo",
         "descripcion": "Recordar llamar por su cumpleaños",
         "estado": "pendiente"
       }
     ]
     ```

2. **POST `/agregar_tarea`**
   - Descripción: Permite agregar una nueva tarea. Se espera un cuerpo en formato JSON con los campos `titulo`, `descripcion` y `estado`.
   - Ejemplo de solicitud:
     ```json
     {
       "titulo": "Estudiar para el examen",
       "descripcion": "Repasar temas de matemáticas",
       "estado": "pendiente"
     }
     ```
   - Ejemplo de respuesta:
     ```json
     {
       "mensaje": "Tarea creada",
     }
     ```

---

## Cómo Usar la Aplicación

1. **Desplegar la aplicación**:
   - Asegúrate de realizar un `push` en la rama `main`.
   - El pipeline se ejecutará automáticamente desplegando la aplicación en AWS EC2.

2. **Probar los endpoints**:
   - Accede al endpoint `/listar_tareas` desde un navegador o herramienta como Postman para obtener la lista de tareas.
   - Utiliza el endpoint `/agregar_tarea` para añadir nuevas tareas mediante solicitudes POST.

---

## Notas Adicionales

- La instancia EC2 debe estar configurada previamente con acceso público al puerto `5000`.
- La URI de MongoDB debe configurarse como un secreto en los ajustes del repositorio (`MONGO_URI`).
- Todos los comandos ejecutados en la instancia EC2 son a través de SSH utilizando las credenciales configuradas en los secretos del repositorio (`EC2_KEY`, `EC2_USER`, `EC2_IP`).

---

**Autor**: Gustavo Auger Gac

# PRACTICAPYTHON

PRACTICAPYTHON es una colección de ejercicios interactivos de lógica de programación creada por Miguel. La intención del proyecto es ofrecer retos claros y prácticos para que estudiantes y autodidactas mejoren su pensamiento algorítmico usando Python y Flask.

Demo: https://practicapython.onrender.com  (pon aquí tu URL real)

## Características
- Ejercicios interactivos con enunciado y formulario para probar soluciones.
- Ejemplos de código en Python (starter code y solución oculta).
- Interfaz responsiva con Bootstrap.
- Video introductorio y página "Acerca de".
- Deploy en Render.

## Tecnologías
- Backend: Python, Flask
- Frontend: Bootstrap, Jinja2
- Deploy: Render
- (Opcional) Resaltado de código: Prism.js

## Instalación (local)
1. Clona el repo:
   ```bash
   git clone https://github.com/miguelprograma200/PRACTICAPYTHON.git
   cd PRACTICAPYTHON
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Variables de entorno (ejemplo .env):
   - `SECRET_KEY`, `PORT` (si usas), credenciales SMTP si aplica.
5. Ejecutar local:
   ```bash
   export FLASK_APP=index.py
   flask run
   ```
   o para producción local con gunicorn:
   ```bash
   gunicorn index:app
   ```

## Despliegue en Render
- Asegúrate de tener `Procfile` con `web: gunicorn index:app`
- Activa Auto Deploy desde la integración con GitHub o usa "Manual Deploy" en el dashboard de Render.

## Cómo contribuir
1. Abre un issue para comentar ideas o bugs.
2. Crea una rama nueva, realiza cambios y abre un Pull Request.
3. Revisa las guías en el README y respeta la convención del proyecto.

## Licencia
Este proyecto está bajo la licencia MIT. Revisa el archivo `LICENSE`.

## Contacto
Miguel — tu-email@example.com  
GitHub: https://github.com/miguelprograma200

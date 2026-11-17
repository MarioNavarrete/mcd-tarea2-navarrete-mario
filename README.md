# MiniChat

**Estudiante:** Mario Navarrete

Aplicación de chat mínima con arquitectura **MVC + Observer**, usada en la
Tarea 2 (Clean Code) del curso Ingeniería de Software (MCD, PUC).

## Instalación (Windows / macOS / Linux)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

No se necesita GPU ni descargar modelos: el backend por defecto es `echo`,
que responde con frases fijas construidas a partir de tu último mensaje.
Es suficiente para verificar manualmente que la aplicación sigue
funcionando después de cada refactorización.

## Ejecutar en consola

```bash
cd src
python -m minichat.app            # backend echo
python -m minichat.app DialoGPT-medium   # requiere torch + transformers
```

## Ejecutar en Jupyter (interfaz con widgets)

Abre `MiniChat_local.ipynb` en Jupyter Lab, o en un notebook nuevo:

```python
import sys
sys.path.append("src")           # ruta a la carpeta src de este repo

from minichat.ui.chat_app import ChatApp
app = ChatApp("echo")
app.show()
```

En Google Colab reemplaza la ruta por `/content/mini-chat/src`.

## Lista de verificación manual (después de cada actividad)

1. Enviar un mensaje con rol `user` y ver que aparece la respuesta del bot.
2. Agregar un mensaje con rol `assistant` y otro con rol `system`.
3. Mover los sliders de generación y enviar otro mensaje (estado "Config updated.").
4. Seleccionar un mensaje y borrarlo con **Delete selected**.
5. **Export JSON** y abrir `chat_transcript.json`.
6. **Delete ALL** y comprobar que la conversación queda vacía.

## Estructura

```
src/minichat/
  app.py                    consola
  core/  observable.py observer.py backend.py
  model/ chat_session.py message.py role.py generation_config.py
         backend_factory.py echo_backend.py dialogpt_backend.py
  controller/ chat_controller.py
  ui/    chat_app.py widgets_view.py history_html.py
```

## Refactorizaciones (Tarea 2)

Cada actividad tiene su propio commit. Después de cada cambio se ejecutó la
lista de verificación manual; `Verificacion.ipynb` contiene la ejecución con
el código final.

| Actividad | Smell | Refactorización | Cambio |
|---|---|---|---|
| A1 | Cadenas mágicas | Replace Magic Literal | `core/events.py` con `Event(str, Enum)`; los literales de eventos se reemplazan por `Event.X`. Un error de tipeo ahora lanza `AttributeError`. |
| A2 | Feature Envy | Usar el método del modelo | `_refresh_selector` usa `m.summary()` en vez de leer `timestamp`, `content` y `role`. |
| A3 | Lista larga de parámetros | Introduce Parameter Object | `set_generation(cfg: GenerationConfig)`; las validaciones pasan a `__post_init__` y la vista usa `dataclasses.replace`, sin repetir el `900`. |
| A4 | Método mal ubicado | Move Method | `last_assistant_text()` pasa de `app.py` a `ChatSession`. |
| A5 | Código muerto | Remove Dead Code | Se eliminan `get_summary` (antes se redirige su único uso en `export_json` a `as_public`), `get_observer_count`, `has_observers`, `_encode_system_message` y `Role.list`. |
| A6 | Condicional extenso | Replace Conditional with Dispatch Table | `on_event` busca el handler en `self._handlers` (un método `_on_...` por evento) e ignora eventos desconocidos. |
| A7 | Método largo (SRP) | Extract Method | `send_user` se divide en `_validate_text` (que ahora trunca a 2000), `_generate_reply` y `_build_meta`. |

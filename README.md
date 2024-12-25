
# Generador de Prompts

Este proyecto genera prompts narrativos personalizados basados en parámetros iniciales. Está diseñado con Streamlit para facilitar la interacción del usuario.

## Funcionalidades

1. **Pantalla 1**: Captura de parámetros iniciales (idea, propósito, estilo, etc.).
2. **Pantalla 2**: Generación, edición y copia del prompt final.
3. **Validaciones**: Los campos obligatorios son verificados para garantizar consistencia.

## Requisitos

- Python 3.11 o superior
- Streamlit 1.22.0

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/generador-prompts.git
   cd generador-prompts
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## Estructura del Proyecto

```
generador-prompts/
├── app.py
├── pantalla1.py
├── pantalla2.py
├── validaciones.py
├── requirements.txt
└── README.md
```

## Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

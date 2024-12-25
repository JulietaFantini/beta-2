
import streamlit as st

def mostrar_pantalla2(params: dict):
    """
    Pantalla 2: Toma todos los campos y genera un prompt narrativo detallado.
    """
    st.title("Pantalla 2: Ajusta y Copia tu Prompt")

    # Generamos el texto base
    prompt_inicial = generar_prompt_narrativo(params)

    st.write("Puedes editar manualmente el prompt a continuación:")
    if "prompt_editable" not in st.session_state:
        st.session_state.prompt_editable = prompt_inicial

    prompt_editable = st.text_area("Prompt Final", value=st.session_state.prompt_editable, height=300, key="prompt_area")

    # Botón para restablecer el prompt inicial
    if st.button("Restablecer Prompt", key="restablecer_prompt"):
        st.session_state.prompt_editable = prompt_inicial
        st.experimental_rerun()

    # Botón para copiar
    if st.button("Copiar Prompt", key="copiar_prompt"):
        copy_to_clipboard(prompt_editable)
        st.success("¡Prompt copiado al portapapeles!")

def generar_prompt_narrativo(params: dict) -> str:
    """
    Concatena los campos en un texto narrativo enriquecido, omitiendo aquellos que estén vacíos o no aporten valor.
    """
    idea = params.get("idea", "")
    proposito = params.get("propósito", "")
    estilo = params.get("estilo", "")
    plano = params.get("plano", "")
    composicion = params.get("composición", "")
    tipo_luz = params.get("tipo_luz", "")
    profundidad = params.get("profundidad_campo", "")
    textura = params.get("textura", "")
    escala = params.get("escala", "")
    estacion = params.get("estación", "")
    efecto = params.get("efecto_visual", "")

    # Construimos la narrativa
    texto = []

    if idea:
        texto.append(f"Imagina {idea}")
    if proposito:
        texto.append(f"con un propósito de {proposito}")
    if estilo:
        texto.append(f"en un estilo {estilo}")
    if plano:
        texto.append(f"capturado en un {plano.lower()}")
    if composicion:
        texto.append(f"con una composición {composicion.lower()}")
    if tipo_luz:
        luz = tipo_luz.lower()
        # Evitar repeticiones de 'luz'
        if "luz" not in luz:
            texto.append(f"e iluminado por {luz}")
        else:
            texto.append(f"iluminado por {luz}")
    if profundidad:
        texto.append(f"mostrando una profundidad de campo {profundidad.lower()}")
    if textura:
        texto.append(f"donde las texturas {textura.lower()} destacan en la escena")
    if escala:
        texto.append(f"a una escala {escala.lower()}")
    if estacion:
        texto.append(f"ambientado en {estacion.lower()}")
    if efecto and efecto.lower() not in ["sin efecto", "none", "", "no efecto"]:
        texto.append(f"y con un efecto de {efecto.lower()}")

    return ", ".join(filter(None, texto)) + "."

def copy_to_clipboard(text: str):
    """
    Hack con JavaScript para copiar 'text' al portapapeles.
    """
    copy_script = f"""
    <script>
    navigator.clipboard.writeText(`{text}`);
    </script>
    """
    st.markdown(copy_script, unsafe_allow_html=True)

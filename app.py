
import streamlit as st
from pantalla1 import configurar_pantalla1
from pantalla2 import mostrar_pantalla2
from validaciones import validar_campos_obligatorios

def main():
    st.set_page_config(page_title="Generador de Prompts", layout="centered")

    # Control básico de navegación
    if "mostrar_pantalla2" not in st.session_state:
        st.session_state.mostrar_pantalla2 = False

    if not st.session_state.mostrar_pantalla2:
        # --- Pantalla 1 ---
        params = configurar_pantalla1()
        st.write("---")
        if st.button("Validar y Continuar", key="validar_continuar"):
            # Validación final
            errores = validar_campos_obligatorios(params)
            if errores:
                st.error("\n".join(errores))
            else:
                # Filtrar parámetros vacíos o irrelevantes antes de avanzar
                valores_excluidos = ["sin efecto", "none", "", "no efecto"]
                params_filtrados = {k: v for k, v in params.items() if v and v.lower() not in valores_excluidos}
                st.session_state.mostrar_pantalla2 = True
                st.session_state.params = params_filtrados
    else:
        # --- Pantalla 2 ---
        params = st.session_state.get("params", {})
        if not params:
            st.warning("No se encontraron datos de Pantalla 1. Por favor, regresa y completa los parámetros.")
        else:
            mostrar_pantalla2(params)

if __name__ == "__main__":
    main()

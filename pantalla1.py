import streamlit as st

def configurar_pantalla1():
    """
    Pantalla 1: Configuración definitiva con parámetros exhaustivos y flujo dinámico.
    """
    if "params" not in st.session_state:
        st.session_state.params = {}

    params = st.session_state.params

    st.title("Pantalla 1: Configura tu Prompt Definitivo")

    # Introducción
    st.info("Selecciona los parámetros clave para personalizar la narrativa, el propósito y los detalles técnicos de tu imagen. Cada opción influye en el estilo, la atmósfera y la composición del resultado generado.")

    # Idea Inicial
    st.subheader("1. Idea Inicial")
    params["idea"] = st.text_input(
        "Describe la idea principal (obligatorio):",
        value=params.get("idea", ""),
        placeholder="Ejemplo: 'Una mujer feliz en un entorno urbano moderno' o 'Un bosque mágico iluminado por luces doradas'"
    )
    if not params["idea"]:
        st.warning("La 'Idea Inicial' es obligatoria.")

    # Movimientos Estéticos (Estilo Artístico)
    st.subheader("2. Estilo Artístico")
    st.write("Define la apariencia visual y la atmósfera de la imagen. Selecciona una categoría de estilo y, si es necesario, especifica un estilo personalizado.")

    estilos_data = {
        'Arte Tradicional': ['Barroco', 'Impresionismo', 'Realismo Fotográfico', 'Cubismo'],
        'Arte Digital Contemporáneo': ['Arte Digital Onírico', 'Fotorrealismo', 'Realismo Cinemático', 'Arte Atmosférico', 'Arte Etéreo'],
        'Estilos Futuristas y Tecnológicos': ['Cyberpunk', 'Neón Futurista', 'Arte Futurista', 'Steampunk'],
        'Diseño Gráfico y Comercial': ['Vectorial', 'Arte Lineal', 'Arte Lineal Minimalista', 'Minimalismo', 'Gráficos Simplificados', 'Diseño Gráfico Complejo'],
        'Estilos Artísticos Especializados': ['Pixel Art', 'Arte Pop', 'Caricaturas Estilizadas', 'Arte Conceptual Técnico', 'Gráficos Técnicos'],
        'Arte Fantástico e Imaginativo': ['Fantasía Épica', 'Surrealismo Clásico', 'Surrealismo Moderno', 'Arte de Fantasía']
    }

    estilo_categoria = st.selectbox(
        "Selecciona una categoría de estilo (obligatorio):",
        list(estilos_data.keys()),
        key="estilo_categoria"
    )
    if estilo_categoria:
        subcategorias = estilos_data[estilo_categoria] + ["Otro"]
        estilo_seleccion = st.selectbox(
            "Selecciona un estilo específico (o elige 'Otro' para personalizar):",
            subcategorias,
            key="estilo_seleccion"
        )
        if estilo_seleccion == "Otro":
            params["estilo_otro"] = st.text_input(
                "Especifica tu estilo personalizado:",
                value=params.get("estilo_otro", "")
            )
            params["estilo"] = params.get("estilo_otro", "").strip()
        else:
            params["estilo"] = estilo_seleccion.strip()

    if not params["estilo"]:
        st.warning("El 'Estilo Artístico' es obligatorio.")

    # Propósito
    st.subheader("3. Propósito")
    st.write("Selecciona una categoría de propósito que defina el uso o contexto de tu imagen. Si el propósito no aparece, elige 'Otro' y personalízalo.")

    usos_data = {
        'Comercial y Marketing': ['Branding Profesional', 'Publicidad Minimalista', 'Campañas Publicitarias Modernas', 'Marketing Visual', 'Catálogos de Productos', 'Ilustración de Productos'],
        'Entretenimiento Digital': ['Videojuegos', 'Storyboarding', 'Diseño Cinematográfico', 'Arte Conceptual Épico', 'Narrativa Épica'],
        'Medios Digitales y Redes Sociales': ['Diseño Gráfico para Redes Sociales', 'Avatares Personalizados', 'Contenido Digital Artístico', 'Caricaturas para Redes Sociales', 'Proyectos Creativos Únicos'],
        'Técnico y Educativo': ['Proyectos Técnicos', 'Diagramas Claros', 'Materiales Educativos', 'Presentaciones Académicas', 'Proyectos STEM', 'Proyectos de Ingeniería Visual'],
        'Arte y Decoración': ['Arte Decorativo', 'Proyectos Artísticos Realistas', 'Arte Naturalista', 'Arte Paisajístico', 'Proyectos Ambientales'],
        'Innovación y Experimentación': ['Proyectos Experimentales', 'Diseño de Futuros Imaginados', 'Branding de Alta Tecnología', 'Proyectos de Diseño Avanzado', 'Arte Retrofuturista']
    }

    uso_categoria = st.selectbox(
        "Selecciona una categoría de propósito (obligatorio):",
        list(usos_data.keys()),
        key="uso_categoria"
    )
    if uso_categoria:
        subcategorias_uso = usos_data[uso_categoria] + ["Otro"]
        uso_seleccion = st.selectbox(
            "Selecciona un propósito específico (o elige 'Otro' para personalizar):",
            subcategorias_uso,
            key="uso_seleccion"
        )
        if uso_seleccion == "Otro":
            params["uso_otro"] = st.text_input(
                "Especifica tu propósito personalizado:",
                value=params.get("uso_otro", "")
            )
            params["propósito"] = params.get("uso_otro", "").strip()
        else:
            params["propósito"] = uso_seleccion.strip()

    if not params["propósito"]:
        st.warning("El 'Propósito' es obligatorio.")

    # Detalles Técnicos (Opcionales)
    if params["estilo"] and params["propósito"]:
        st.subheader("4. Detalles Técnicos (Opcionales)")
        st.write("Explora opciones para personalizar los detalles técnicos y enriquecer tu imagen con precisión narrativa.")

        # Plano Fotográfico
        st.subheader("4.1 Plano Fotográfico")
        st.write("El plano fotográfico establece la relación visual entre el sujeto y su entorno. Selecciona una opción que complemente tu narrativa.")
        plano = st.selectbox(
            "Selecciona un plano fotográfico:",
            ["Primer Plano", "Plano Medio", "Plano General", "Cenital", "Contrapicado", "Otro"],
            key="plano"
        )
        if plano == "Otro":
            params["plano"] = st.text_input(
                "Especifica tu plano personalizado:",
                value=params.get("plano", "")
            )
        else:
            params["plano"] = plano.strip()

        # Validación de compatibilidad entre plano y escala
        st.subheader("4.2 Escala")
        st.write("La escala define la proporción visual y la importancia de los elementos en la escena.")
        escala = st.selectbox(
            "Selecciona la escala:",
            ["Monumental", "Realista", "Íntima", "Otro"],
            key="escala"
        )
        if escala == "Otro":
            params["escala"] = st.text_input(
                "Especifica la escala personalizada:",
                value=params.get("escala", "")
            )
        else:
            params["escala"] = escala.strip()

        if params.get("plano") == "Primer Plano" and params.get("escala") == "Monumental":
            st.warning("Seleccionar 'Primer Plano' con 'Escala Monumental' podría generar inconsistencias visuales.")

        # Tipo de Luz
        st.subheader("4.3 Tipo de Luz")
        st.write("El tipo de luz influye en la atmósfera y el estado de ánimo de la imagen. Selecciona una iluminación que resalte tu narrativa.")
        tipo_luz = st.selectbox(
            "Selecciona el tipo de luz:",
            ["Luz Suave", "Luz Dura", "Contraluz", "Luz Neón", "Otro"],
            key="tipo_luz"
        )
        if tipo_luz == "Otro":
            params["tipo_luz"] = st.text_input(
                "Especifica el tipo de luz personalizada:",
                value=params.get("tipo_luz", "")
            )
        else:
            params["tipo_luz"] = tipo_luz.strip()

        # Textura
        st.subheader("4.4 Textura")
        st.write("La textura añade realismo visual y sensorial a los elementos de la imagen. Define cómo se percibe la superficie.")
        textura = st.selectbox(
            "Selecciona la textura:",
            ["Suave", "Metálica", "Rugosa", "Otro"],
            key="textura"
        )
        if textura == "Otro":
            params["textura"] = st.text_input(
                "Especifica la textura personalizada:",
                value=params.get("textura", "")
            )
        else:
            params["textura"] = textura.strip()

        # Efecto Visual
        st.subheader("4.5 Efecto Visual")
        st.write("Los efectos visuales refuerzan la atmósfera de la imagen y pueden añadir un toque estilístico único.")
        efecto_visual = st.selectbox(
            "Selecciona el efecto visual:",
            ["Reflejos", "Neón", "Desenfoque", "Otro"],
            key="efecto_visual"
        )
        if efecto_visual == "Otro":
            params["efecto_visual"] = st.text_input(
                "Especifica el efecto visual personalizado:",
                value=params.get("efecto_visual", "")
            )
        else:
            params["efecto_visual"] = efecto_visual.strip()

    # Botón para Validar y Continuar
    if st.button("Validar y Continuar"):
        errores = []
        if not params["idea"]:
            errores.append("El campo 'Idea Inicial' está vacío.")
        if not params["estilo"]:
            errores.append("El campo 'Estilo Artístico' está vacío o no es válido.")
        if not params["propósito"]:
            errores.append("El campo 'Propósito' está vacío o no es válido.")

        if errores:
            st.error("\n".join(errores))
        else:
            st.session_state.mostrar_pantalla2 = True

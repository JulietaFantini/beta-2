
def validar_campos_obligatorios(params: dict) -> list:
    """
    Verifica que 'idea_inicial', 'propósito' y 'estilo' no estén vacíos ni en 'Selecciona una opción'.
    Retorna una lista de errores si algo falla.
    """
    errores = []
    obligatorios = ["idea", "propósito", "estilo"]

    for campo in obligatorios:
        val = params.get(campo, "").strip()
        if not val or val.lower() == "selecciona una opción":
            errores.append(f"El campo '{campo}' es obligatorio y no puede estar vacío.")

    return errores

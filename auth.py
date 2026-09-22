"""
Módulo de autenticación y control de accesos de NovaSoft.
"""

USUARIOS_AUTORIZADOS = {
    "admin": "hash_admin_token",
    "operador": "hash_operador_token"
}

def autenticar_usuario(usuario: str, token: str) -> bool:
    if usuario in USUARIOS_AUTORIZADOS:
        return USUARIOS_AUTORIZADOS[usuario] == token
    return False

def tiene_permiso(usuario: str, rol_requerido: str) -> bool:
    roles = {
        "admin": ["CREAR", "MODIFICAR", "ELIMINAR", "CONSULTAR"],
        "operador": ["CREAR", "CONSULTAR"]
    }
    return rol_requerido in roles.get(usuario, [])
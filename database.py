"""
Módulo de persistencia y conexión a base de datos de NovaSoft.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "novasoft_user",
    "password": "secure_password",
    "database": "pedidos_db"
}

def conectar_db():
    print(f"[*] Conectando a PostgreSQL en {DB_CONFIG['host']}:{DB_CONFIG['port']}...")
    return {"status": "connected", "database": DB_CONFIG["database"]}

def desconectar_db():
    print("[*] Conexión cerrada exitosamente.")
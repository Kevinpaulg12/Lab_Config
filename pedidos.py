"""
Módulo principal de gestión de pedidos.
"""

def crear_pedido(id_pedido: int, cliente: str, productos: list):
    return {
        "id_pedido": id_pedido,
        "cliente": cliente,
        "items": productos,
        "estado": "CREADO"
    }

def calcular_total_pedido(items: list) -> float:
    # Código estable: suma de precios unitarios por cantidad
    total = sum(item["precio"] * item["cantidad"] for item in items)
    return round(total, 2)

def actualizar_estado(pedido: dict, nuevo_estado: str):
    estados_validos = ["CREADO", "PROCESANDO", "ENVIADO", "ENTREGADO", "CANCELADO"]
    if nuevo_estado in estados_validos:
        pedido["estado"] = nuevo_estado
        return pedido
    raise ValueError("Estado no permitido")
class Pedido:
    def __init__(self, id_pedido: int, cliente: str, items: list):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.items = items
        self.estado = "CREADO"

    def calcular_total(self) -> float:
        return round(sum(item["precio"] * item["cantidad"] for item in self.items), 2)

    def actualizar_estado(self, nuevo_estado: str):
        estados_validos = ["CREADO", "PROCESANDO", "ENVIADO", "ENTREGADO", "CANCELADO"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no permitido")
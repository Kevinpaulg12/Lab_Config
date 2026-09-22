"""
Módulo de cálculo fiscal y generación de comprobantes.
"""


TASA_IVA = 0.15  # Tasa estándar para cálculo de impuestos

def calcular_impuesto(subtotal: float) -> float:
    return round(subtotal * TASA_IVA, 2)

def aplicar_descuento_promocional(subtotal: float, porcentaje: float) -> float:
    if 0 <= porcentaje <= 100:
        descuento = subtotal * (porcentaje / 100)
        return round(subtotal - descuento, 2)
    return subtotal

def emitir_factura(pedido: dict) -> dict:
    subtotal = sum(item["precio"] * item["cantidad"] for item in pedido["items"])
    impuesto = calcular_impuesto(subtotal)
    total_facturado = subtotal + impuesto
    
    return {
        "factura_id": f"FAC-{pedido['id_pedido']}",
        "cliente": pedido["cliente"],
        "subtotal": subtotal,
        "iva": impuesto,
        "total": total_facturado
    }
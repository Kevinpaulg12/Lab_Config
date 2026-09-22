"""
Punto de entrada de la aplicación NovaSoft - Sistema de Pedidos.
"""

from database import conectar_db, desconectar_db
from pedidos import crear_pedido, calcular_total_pedido
from facturacion import emitir_factura
from auth import autenticar_usuario

def main():
    print("=== INICIANDO SISTEMA NOVASOFT V1.0.0 ===")
    
    # 1. Conexión
    conectar_db()
    
    # 2. Autenticación
    if not autenticar_usuario("admin", "hash_admin_token"):
        print("[!] Acceso denegado.")
        return

    # 3. Creación y cálculo de pedido
    items_ejemplo = [
        {"nombre": "Teclado Mecánico", "precio": 45.50, "cantidad": 2},
        {"nombre": "Mouse Inalámbrico", "precio": 25.00, "cantidad": 1}
    ]
    pedido = crear_pedido(101, "Acme Corp", items_ejemplo)
    subtotal = calcular_total_pedido(items_ejemplo)
    
    print(f"[+] Pedido #{pedido['id_pedido']} registrado para {pedido['cliente']}.")
    print(f"[+] Subtotal calculado: ${subtotal}")

    # 4. Facturación
    factura = emitir_factura(pedido)
    print(f"[+] Factura emitida: {factura['factura_id']} | Total con IVA: ${factura['total']}")
    
    # 5. Cierre
    desconectar_db()
    print("=== SISTEMA FINALIZADO CON ÉXITO ===")

if __name__ == "__main__":
    main()
""" ¿Cuánto saldo le quedaría si la operación se autoriza?
¿Cuánto límite diario le queda disponible antes de esta operación?
¿Se debe autorizar o rechazar la operación? Explica por qué."""


def verificar_operacion(operacion):
    autorizacion = ""
    motivo = ""
    limite = operacion["limite_diario"]-operacion["gastado_hoy"]
    saldo = operacion["saldo"]
    
    if operacion["usuario_activo"]:
        autorizacion = True
        if not operacion["cuenta_bloqueada"]:
            autorizacion = True
            if operacion["monto"] <= limite and operacion["saldo"] >= operacion["monto"] and operacion["monto"] > 0:
                saldo -= operacion["monto"]
                limite -= operacion["monto"]
                operacion["gastado_hoy"] += operacion["monto"]
            elif operacion["monto"] > limite:   
                autorizacion = False
                motivo = "Monto excede el límite diario."
            elif operacion["monto"] > saldo:
                autorizacion = False
                motivo = "Saldo insuficiente."
            elif operacion["monto"] <= 0:
                autorizacion = False
                motivo = "Monto inválido. Debe ser mayor a cero."
                
        else:
           autorizacion = False
           motivo = "Cuenta bloqueada. No se puede realizar la operación."
    else:
        autorizacion = False
        motivo = "Usuario inactivo. No se puede realizar la operación."

    
    
    return {
        "autorizacion": autorizacion,
        "motivo": motivo,
        "saldo_restante": saldo,
        "limite_restante": limite
    }



operacion = {
    "usuario_activo": True,
    "cuenta_bloqueada": False,
    "saldo": 1500,
    "monto": -100,
    "limite_diario": 2000,
    "gastado_hoy": 900
}


resultados = verificar_operacion(operacion)

print("Autorización:", resultados["autorizacion"])
print("Motivo:", resultados["motivo"])
print("Saldo restante:", resultados["saldo_restante"])
print("Limite restante:", resultados["limite_restante"])

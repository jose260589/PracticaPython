def pedidos_detalle(pedidos):
    pedidos_pagados = 0
    sumatoria_total_pagado = 0
    pedidos_pendientes = 0
    pedido_mayor = 0
    cliente_mayor = ""

    
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = pedido["total"]
        estado = pedido["estado"]

        if(estado == "pagado"):
            pedidos_pagados += 1
            sumatoria_total_pagado += total

            if(total > pedido_mayor):
                pedido_mayor = total
                cliente_mayor = cliente


        if(estado == "pendiente"):
            pedidos_pendientes += 1

    print("Cantidad de pedidos pagados:", pedidos_pagados)
    print("Sumatoria total de pedidos pagados:", sumatoria_total_pagado)
    print("Cantidad de pedidos pendientes:", pedidos_pendientes)
    print("Cliente con el pedido mayor:", cliente_mayor, "con un total de:", pedido_mayor)



pedidos = [
    {"cliente": "Ana", "total": 1200, "estado": "pagado"},
    {"cliente": "Luis", "total": 800, "estado": "pendiente"},
    {"cliente": "Pedro", "total": 2500, "estado": "pagado"},
    {"cliente": "Maria", "total": 450, "estado": "cancelado"},
    {"cliente": "Carlos", "total": 1800, "estado": "pagado"}
]

pedidos_detalle(pedidos)
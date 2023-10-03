mesaCliente = input("ingrese numero de la mesa ")
costoPedido = int(input("ingrese el costo del pedido "))
costoImpuesto = (costoPedido*0.1)
costoTotal = costoPedido + costoImpuesto
costoPedidoStr = str(costoPedido)
costoImpuestoStr = str(costoImpuesto)
costoTotalStr = str(costoTotal)
print("El costo toal del pedido para la mesa "+ mesaCliente +" es: " + costoPedidoStr + 
      " .El impuesto del 10% pedido es " + costoImpuestoStr + " y el valor total del pedido mas el impuesto es " + costoTotalStr + ".")




tipo_de_cambio_eur_mxn = 23.70
tipo_de_cambio_usd_mxn = 20.75


tipo_cambio = input("Ingrese la moneda a conveir EUR o USD ")

valor_cambio = float(input("Ingrese el valor a convertir "))

if tipo_cambio.upper() == "EUR":
    resultado = tipo_de_cambio_eur_mxn * valor_cambio
    print("El resultado de la convercion de EUR a MXN es ", resultado)
elif tipo_cambio.upper() == "USD":
    resultado = tipo_de_cambio_usd_mxn * valor_cambio
    print("El resulutado de la conversion de USD a MXN es ", resultado)
else:
    print("Ese tipo de cambio no esta disponible")

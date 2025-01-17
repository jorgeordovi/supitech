# supitech
Evaluar errores de calculo
Evaluar las perdidas financeirasprecicion delas concveriones 
posibles erores calculos en los usarios
soluciones alernativas

Definir valor actual EUR-MXN y USD-MXN
definir tipo_cambio_eur_mxn = 23.70 # consumir datos de DB o API
definir tipo_cambio_usd_mxn = 20.75

Prompt: 
 "Ingrese USD o EUR segun el valor a convertir"
guardar en variable = tipo_de_cambio

Prompt:
 "Ingrese el valor en numeros enteros"
guardar en variable - valor_de_cambio
Realize the conversion == "EUR"
    Calcular resultado = monto_a_converir * tipo_cambio_eur_mxn
    retrurn("El resultado de la conversion EUR a MXN es ")
elseif:
    Calcular resultado = valor_de_cambio * tipo_de_cambio_usd_mxn
else:
    "mostrar no esa disponible ese tipo de cambio
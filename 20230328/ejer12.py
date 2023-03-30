# El sobrino de nuestro vecino pintor quiere controlar lo que le pagan por mes.

horas_trabajadas = int(input('Ingresar las horas trabajadas: '))
horas_extras_trabajadas = int(input('Ingresar las horas extras trabajadas: '))
pago_horas = int(input('Ingresar pago por hora: '))

PORSENTAJE_EXTRAS_HORAS = 40
PORSENTAJE_DESCUENTO_OBRA_SOCIAL = 6
PORSENTAJE_DESCUENTO_JUVILATORIO = 11
PORSENTAJE_HORAS_AUMENTO = 17


total_pago_horas_trabajadas = horas_trabajadas * pago_horas

pago_horas_extra = pago_horas + (pago_horas * (PORSENTAJE_EXTRAS_HORAS / 100))

total_pago_horas_extra_trabajadas = pago_horas_extra * horas_extras_trabajadas

total_pago_horas = total_pago_horas_extra_trabajadas + total_pago_horas_trabajadas

descuento_juvilatorio = total_pago_horas * (PORSENTAJE_DESCUENTO_JUVILATORIO / 100)
descuento_obra_social = total_pago_horas * (PORSENTAJE_DESCUENTO_OBRA_SOCIAL / 100)

total_descuentos = descuento_juvilatorio + descuento_obra_social

total_pago_extra = total_pago_horas_trabajadas * (PORSENTAJE_HORAS_AUMENTO / 100)

total_pago = total_pago_horas - total_descuentos + total_pago_extra

recivo = f"""
Horas trabajadas: \t{horas_trabajadas}
Horas extra: \t{horas_extras_trabajadas}
Pago por hora: \t{pago_horas}
hs \t{horas_trabajadas} \t{pago_horas} \t{total_pago_horas_trabajadas}
extra \t{horas_extras_trabajadas} \t{pago_horas_extra} \t{total_pago_horas_extra_trabajadas}
{total_pago_horas}
jubilación \t{PORSENTAJE_DESCUENTO_JUVILATORIO}% \t{descuento_juvilatorio}
obra social \t{PORSENTAJE_DESCUENTO_OBRA_SOCIAL}% \t{descuento_obra_social}
{total_descuentos}
extra \t{PORSENTAJE_HORAS_AUMENTO}% \t{total_pago_extra}
{total_pago}
"""

print(recivo)

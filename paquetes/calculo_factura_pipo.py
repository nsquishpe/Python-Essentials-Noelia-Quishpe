# -*- coding: utf8 -*-

from tostadas_pipo.utilidades import calculos
from tostadas_pipo.utilidades.impuestos import impuesto_iva14

monto = 2
monto_suma = 3

suma = impuesto_iva14(monto) + calculos.suma_total(monto_suma)

print ("Total a Facturar: {0} BsS, con IVA 14%.".format(suma) )

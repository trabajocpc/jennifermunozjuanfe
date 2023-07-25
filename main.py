import pandas as pd
from data.platos import platosPopulares
from helpers.crearTabla import crearTabla

from data.reserva import reservas
from data.proveedores import proveedores

tablaPlatos=pd.DataFrame(platosPopulares)
crearTabla(tablaPlatos,"platos")

tablaReservas=pd.DataFrame(reservas)
crearTabla(tablaReservas,"tablaReservas")

tablaproveedores=pd.DataFrame(proveedores)
crearTabla(tablaproveedores,"tablaproveedores")
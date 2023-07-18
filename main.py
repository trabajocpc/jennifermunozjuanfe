import pandas as pd
from data.platos import platosPopulares
from helpers.crearTabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
crearTabla(tablaPlatos,"platos")
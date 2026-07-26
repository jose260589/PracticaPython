#pruebas de tipos de datos de fechas.
### Dates ###
#llamar a la función datetime.now()
from datetime import datetime
#inicializar variable now con la fecha y hora actual
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


timestamp = now.timestamp()
print(timestamp)

year_2027 = datetime(2027, 1, 1)
print(year_2027)

from datetime import time

#current_time = time() #se puede poner vacio, pero da valor 00:00:00
current_time = time(12, 30, 45)
print("Time: ")
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
#current_date = date() #se puede poner vacio, pero da valor 0001-01-01
current_date = date(2026, 7, 25)
print("Date: ")
print(current_date.year)
print(current_date.month)
print(current_date.day)

""" 
se puede restar fechas por lo normal tienen que ser del mismo tipo, si no da error.
"""

from datetime import timedelta

delta = timedelta(days=5, hours=3, minutes=30)
print("Timedelta")
print(delta)

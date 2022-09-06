import datetime
fecha = datetime.datetime.now()

print ('Hoy es:',fecha.strftime('%d/%m/%Y'))

import socket
host = socket.gethostname()

print('Mi nombre de host es %s' %host)

print ("voy a Iterar 10 veces")
for i in range(10):
   print ("Iteracion:",i)

print ("FIN")

exit()

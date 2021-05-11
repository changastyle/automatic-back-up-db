import os
from datetime import datetime


archivoConfig = open("config-back-up-dbs.conf", "r")
for lineaLoop in archivoConfig:
      lineaLoop = lineaLoop.strip()
      print("----------------------")
      print(lineaLoop)

      # schema = "ecommerce"
      schema = lineaLoop
      print("schema:" + str(schema))
      ahora = datetime.now()

      ahoraFormateadoHumano = ahora.strftime("%d-%m-%Y_%H-%M")
      print("ahora =", ahoraFormateadoHumano)

      nombreArchivo = schema + "_" + ahoraFormateadoHumano
      comando  = "mysqldump --defaults-extra-file=D:\DATOS\Descargas\chota.pass " + schema + " > D:\DATOS\Escritorio\\" + nombreArchivo + ".sql"
      print("comando:" + str(comando))
      os.system("cmd /c "+ comando + "")
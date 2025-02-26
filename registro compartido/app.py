from multiprocessing.managers import BaseManager
from multiprocessing import Manager, Process, freeze_support
from queue import Queue
import time

clientes = []

def monitor():
    while(True):
        print('hay', len(clientes), "conectados")
        time.sleep(2)
    
def registrar_conexion(datos):
    clientes.append(datos)
    
def registrar_desconexion(datos):
    clientes.pop(datos)
    
class MyManager(BaseManager):
    pass
    
if __name__ == "__main__":
    freeze_support()
    clientes = Manager().list()
    MyManager.register("get_registro", callable=registrar_conexion)
    MyManager.register("get_desconexion", callable=registrar_desconexion)
    
    manag = MyManager(address=("localhost", 5000), authkey=b'123')
    manag.start()
    p1 = Process(target=monitor, daemon=True)
    p1.start()
    try:
        while(True):
            print("servidor en servicio")
            time.sleep(2)
    except KeyboardInterrupt:
        print("servidor detenido")
        
    finally:
        manag.shutdown()
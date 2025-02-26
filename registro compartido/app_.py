from multiprocessing.managers import BaseManager
from multiprocessing import Manager, Process, freeze_support, Queue
import time

class RegistroCompartido:
    def __init__(self):
        self.clientes = Manager().list()
        self.queue = Queue()
        self.veces_checado = 0
        
    def checar(self):
        print(f"checado y verificado {self.veces_checado + 1} veces.")
        self.veces_checado += 1
        
    def get_queue(self):
        return self.queue
        
    def registrar_conexion(self, datos):
        self.clientes.append(datos)
    
    def registrar_desconexion(self, datos):
        if datos in self.clientes:
            self.clientes.remove(datos)
    
    def get_clientes(self):
        return self.clientes
    
    def __call__(self):
        return self

clientes = []

def monitor(registroCompartido):
    registroCompartido.checar()
    while(True):
        print('hay', len(registroCompartido.get_clientes()), "conectados")
        time.sleep(2)
    
class MyManager(BaseManager):
    pass
    
if __name__ == "__main__":
    freeze_support()
    clientes = Manager().list()
    
    registroCompartido = RegistroCompartido()
    
    MyManager.register("registroCompartido", callable=registroCompartido)
    manag = MyManager(address=("localhost", 5000), authkey=b'123')
    manag.start()
    p1 = Process(target=monitor, daemon=True, args=(registroCompartido,))
    p1.start()
    try:
        while(True):
            print("servidor en servicio")
            time.sleep(2)
    except KeyboardInterrupt:
        print("servidor detenido")
        
    finally:
        manag.shutdown()
from multiprocessing.managers import BaseManager
import time

class ClientManager(BaseManager):
    pass

ClientManager.register('registroCompartido')

# Conectar con el servidor
manager = ClientManager(address=('localhost', 5000), authkey=b'123')
manager.connect()

registroCompartido = manager.registroCompartido()
registroCompartido.checar()
registroCompartido.get_queue().put("hola app2.py")

registroCompartido.registrar_conexion("1")
time.sleep(5)
registroCompartido.registrar_desconexion("1")
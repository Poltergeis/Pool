from multiprocessing.managers import BaseManager
from queue import Queue

BaseManager.register('get_mycola')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'abcd')
manager.connect()
mycola:Queue = manager.get_mycola()
mycola.put("hola")
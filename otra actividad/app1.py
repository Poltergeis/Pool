from multiprocessing.managers import BaseManager
from queue import Queue
import time

myCola = Queue()
BaseManager.register('get_mycola', callable=lambda:myCola)
manager = BaseManager(address=('', 5000), authkey=b'abcd')
s_manager = manager.get_server()
s_manager.serve_forever()
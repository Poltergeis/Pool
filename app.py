import random
import time
from multiprocessing import Pool

def factorial(x):
    f = 1
    for i in range(2, x - 1):
        print("generando", i, "def factorial", x)
        f *= i
        time.sleep(random.uniform(0.25, 2.5))
    
    return f

if __name__ == "__main__":
    print("iniciando el proceso", time.strftime('%X'))
    start = time.time()
    pl = Pool(4)
    rs = pl.imap(factorial, [2,20,40,50])
    print("estoy haciendo otra cosa")
    print("los factoriales son", rs.next())
    print("terminando a las", time.strftime('%X'))
    end = time.time()
    print("tiempo total", end - start)
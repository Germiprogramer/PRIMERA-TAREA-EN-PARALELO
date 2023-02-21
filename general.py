from multiprocessing import Pool
from time import sleep
import time
import random

def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
urls = ["a.com", "b.com", "c.com", "d.com"]

def calcular_tiempo_secuencial(urls):
    tiempo_total = 0
    for url in urls:
        tiempo_total += scrape(url)[1]
    return tiempo_total

def ejemplo_secuencial():
        
        tiempo_inicial = time.time()
        
        print("EJEMPLO SECUENCIAL")

        calcular_tiempo_secuencial(urls)

        print(time.time() - tiempo_inicial, "segundos")

        

def ejemplo_multiprocesamiento():
        print("EJEMPLO EN MULTIPROCESAMIENTO")

        tiempo_inicial = time.time()

        pool = Pool(processes=4)
        data = pool.map(scrape, urls)
        pool.close()    
        print()
        for row in data:
            print(row)

        print(time.time() - tiempo_inicial, "segundos")


if __name__ == "__main__":
     
     ejemplo_secuencial()

     ejemplo_multiprocesamiento()


from multiprocessing import Pool
from time import sleep
import time
import random

tiempo_inicial = time.time()

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

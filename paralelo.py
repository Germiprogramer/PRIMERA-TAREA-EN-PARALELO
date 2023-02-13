#urls 
urls = ["a.com", "b.com", "c.com", "d.com"]

# funcion para raspar urls
import random
from time import sleep
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

# hacer el trabajo secuencialmente

def calcular_tiempo_secuencial(urls):
    tiempo_total = 0
    for url in urls:
        tiempo_total += scrape(url)[1]
    return tiempo_total

# hacer el trabajo con multiprocesamiento

from multiprocessing import Pool

pool = Pool(processes=4)

#data = pool.map(scrape, urls)

#pool.close()

#for row in data:
 #   print(row)













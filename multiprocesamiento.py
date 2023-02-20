from general import *

if __name__ == "__main__":
  
    print("EJEMPLO EN MULTIPROCESAMIENTO")

    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)

    print(time.time() - tiempo_inicial, "segundos")
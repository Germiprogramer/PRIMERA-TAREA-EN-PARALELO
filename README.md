# PRIMERA-TAREA-EN-PARALELO

El link al repositorio al repositorio: https://github.com/Germiprogramer/PRIMERA-TAREA-EN-PARALELO.git

# Programacion secuencial

La programación secuencial consiste en que una tarea sigue a la otra y esta a su vez a otra y se van ejecutando consecutivamente.

# Multiprocesamiento

El multiprocesamiento son múltiples procesos que se ejecutan utilizando  uno o mas procesadores. 

# Ejecución del programa

      EJEMPLO SECUENCIAL
      starting a.com
      finished a.com time taken: 0.122 seconds
      starting b.com
      finished b.com time taken: 0.814 seconds
      starting c.com
      finished c.com time taken: 0.417 seconds
      starting d.com
      finished d.com time taken: 0.73 seconds
      2.1109232902526855 segundos
      EJEMPLO EN MULTIPROCESAMIENTO
      starting a.com
      starting b.com
      starting c.com
      starting d.com
      finished b.com time taken: 0.197 seconds
      finished a.com time taken: 0.344 seconds
      finished c.com time taken: 0.497 seconds
      finished d.com time taken: 0.514 seconds

      ('a.com', 0.344)
      ('b.com', 0.197)
      ('c.com', 0.497)
      ('d.com', 0.514)
      0.9050920009613037 segundos

# Conclusiones

En las distintas pruebas que se han hecho, y tal y como se ve en el ejemplo de ejecución del programa, la ejecución con multiprocesamiento es más rápida que la secuencial. Esto se debe a que los procesos se ejecutan todos a la vez, y como no tienen ninguna relación directa entre sí, la programación secuencial es menos adecuada para este caso.

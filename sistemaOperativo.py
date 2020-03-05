#Javier Estuardo Hernández 19202

import simpy
import random

def proceso(env, time, RAM, CPU):
    
    intervalo = 10
    random.expovariate(1.0 / intervalo)
    
    horaInicio = env.now
    yield env.timeout(time)
    
    #fase new
    #solicitud de memoria y el tiempo que pasa en espera de memoria
    memoriaRequerida = random.randint(1, 10)
    RAM.get(memoriaRequerida)
    yield env.timeout(memoriaRequerida)
    #print(nombre + "necesita " + memoriaRequerida + "de memoria.")
    
    if(memoriaRequerida < RAM.level):
        #pasa a fase ready
        usarCpu = random.randint(1, 10)
        yield env.timeout(usarCpu)
        
        if(usarCpu <= 3):
            #pasa a fase running
            yield env.timeout(5)
            RAM.put(memoriaRequerida)
        else:
            #esperar a ser atendido por el CPU
            yield env.timeout(5)
            RAM.put(memoriaRequerida)
    else:
        yield env.timeout(5)
        RAM.put(memoriaRequerida)
        

#---------------------------------------------------------    
env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env, capacity = 1)
random.seed(10) # fijar el inicio de random

for i in range(5):
    env.process(proceso(env, random.expovariate(1.0/10), RAM, CPU))

env.run(until=200)
#no muestra nada

#al descomentar el print, muestra 'None'
#print(env.run(until = 200))

#Las gráficas son inventadas, preferí entregar algo a nada
#pero no sé si valdrá la pena...

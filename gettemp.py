from gpiozero import CPUTemperature
import time


x = int(input('Number of Repeats ---------------- '))
y = int(input('How often it pulls temp (sec) ---- '))


i = 1
while i < x:
    
    cpu = CPUTemperature()
    cpufinal = CPUTemperature()

    time.sleep(y)
    
    cpu = int(cpu.temperature)
    
    graph = cpu #or //2 or //5
    
    graph = int(cpu)

    print(graph *'-')
    print(cpufinal)

    i = i + 1

print('''
The Tracking has completed ''')
 

#add a bar chart by for in the tens and the ones place by ----- 
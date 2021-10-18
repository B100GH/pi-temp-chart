from gpiozero import CPUTemperature
import time


x = int(input('Number of Repeats ---------------- '))
y = int(input('How often it pulls temp (sec) ---- '))


i = 1
while i < x:
    
    cpu = 0
    cpufinal = 0

    cpu = CPUTemperature()
    cpufinal = CPUTemperature()
    cpufinal = cpu.temperature

    time.sleep(y)
    
    cpu = int(cpu.temperature)
    
    graph = cpu #or //2 or //5 use for scale of graph
    
    graph = int(cpu)

    cpufinal = str(cpufinal)

    a = ((graph *'-')+("      "+cpufinal))

    print(a)

    text_file = open("/home/pi/desktop/temprecords.txt","a")
    text_file.write(a+'''
    ''')
    text_file.close()

    i = i + 1

print('''
The Tracking has completed ''')
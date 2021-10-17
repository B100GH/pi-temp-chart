from gpiozero import CPUTemperature
import time

i = 1
while i <=60:
    
    time.sleep(60) # Sleep for 60 seconds
    
    
    cpu = CPUTemperature()
    print(print(cpu.temperature))
    i = i + 1

print('''
done
''')

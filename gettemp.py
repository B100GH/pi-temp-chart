from gpiozero import CPUTemperature
import time


x = int.input('Number of Repeats -- ')
y = int.input('How often it pulls temp (sec) -- ')


i = 1
while i <=x:
    
    time.sleep(y) # Sleep for 60 seconds
    
    
    cpu = CPUTemperature()
    print(print(cpu.temperature))
    i = i + 1

print('''
done
''')

print(x + )
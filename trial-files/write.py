import serial
import time
#port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
for i in range(1, 100):
    print(i)
    port.write(bytes('abhsihek  '+str(i),'utf-8'))
    time.sleep(2)
    
port.close()

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                


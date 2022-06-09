import serial
import time

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
moves = []

ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
time.sleep(2)
ser.write(b'0')
count=0
while (True):
    if (ser.inWaiting()>0):
        count += 1
        current = ser.readline().strip()
        if not current.strip():
            continue
        moves.append(current)    
        print(current)
        print ([moves])
        #check for flag and if found write to serial
        if (current == b'S'): #SensorDetected:
            print("resetting")
            ser.write(b'#Reset#')
            for i in reversed(moves):
                print(i)
                ser.write(i + b'#')
            moves = []




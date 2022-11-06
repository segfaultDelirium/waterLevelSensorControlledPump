import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
serialInst.baudrate = 9600

portList = list()

for i, port in enumerate(ports):
    portList.append(str(port))
    print( f'{i=};  {port}.')

val = input("select port: ")
chosenPort = portList[int(val)]
print(f'{chosenPort=}')

serialInst.port = chosenPort
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))
import serial.tools.list_ports

serialInst = serial.Serial()


def select_port():
    ports = serial.tools.list_ports.comports()
    serialInst.baudrate = 9600

    port_list = list()

    for i, port in enumerate(ports):
        port_list.append(port.device)
        print(f'{i=};  {port.device}.')

    val = input("select port: ")
    chosen_port = port_list[int(val)]
    print(f'{chosen_port=}')
    return chosen_port


serialInst.port = select_port()
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))

# while True:
#     if serialInst.in_waiting:
#         packet = serialInst.readline()
#         print(packet.decode('utf'))
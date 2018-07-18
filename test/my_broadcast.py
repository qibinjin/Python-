
import socket, time

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    udp_socket.bind(('', 9999))
    send_data = 'llll\n'.encode('gbk')

    udp_socket.sendto(send_data, ('255.255.255.255', 8989))
    time.sleep(1)
    udp_socket.close()
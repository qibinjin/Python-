import socket, threading


def send_data(udp_socket):
    data = input('please input data').encode('gbk')
    udp_socket.sendto(data, ('192.168.164.22', 8888))


def recv_data(udp_socket):
    while True:
        data, ip_part = udp_socket.recvfrom(1024)
        print(data.decode('gbk'))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('', 9999))

    recv_thread = threading.Thread(target=recv_data, args=(udp_socket,), daemon=True)

    recv_thread.start()
    while True:
        index = input('please choose 1.send message ,2. quit')

        if index == '1':
            send_data(udp_socket)
        elif index == '2':
            print('see you next time!')
            break

    udp_socket.close()


if __name__ == '__main__':
    main()

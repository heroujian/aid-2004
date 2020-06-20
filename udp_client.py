"""
udp_client.py  udp套接字流程客户端演示
重点代码
"""

from socket import *

# 访问服务器的地址
ADDR = ('172.40.91.178',8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    # 发送消息
    msg = input(">>")
    # 结束循环
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)
    # 接收消息
    msg,addr = udp_socket.recvfrom(1000)
    print("从服务端收到:",msg.decode())

# 关闭套接字
udp_socket.close()

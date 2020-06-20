"""
udp_server.py  udp套接字服务端流程
重点代码
"""
from socket import *

# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(("0.0.0.0",8888))

while True:
    # 接收消息
    data,addr = sockfd.recvfrom(1000)
    print(addr,"接收到:",data.decode()) # data是字节串
    # 发送消息
    n = sockfd.sendto(b"Thanks",addr) # 发送字节串
    print("发送了%d bytes"%n)

# 关闭套接字
sockfd.close()


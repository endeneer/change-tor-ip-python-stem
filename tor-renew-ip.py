import time
import socket
import socks

from urllib.request import urlopen
from stem import Signal
from stem.control import Controller

controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renewTor():
    controller.authenticate("abc123")
    controller.signal(Signal.NEWNYM)

def showIP():
    print(urlopen('https://icanhazip.com').read())

for i in range(5):
    renewTor()
    connectTor()
    showIP()
    time.sleep(10)



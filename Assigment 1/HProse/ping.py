import socket
import subprocess
import hprose


def ping():
    hostname = socket.gethostname()
    ping_result = subprocess.run(['ping', '-c', '1', hostname], capture_output=True)
    if ping_result.returncode == 0:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    else:
        return None


server = hprose.HttpServer(port=8083)
server.addFunction(ping)
server.start()

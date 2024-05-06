import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(1)
            resposta = client.connect_ex((host, port))
            if resposta == 0:
                print(f"A porta {port} em {host} está aberta.")
            else:
                print(f"A porta {port} em {host} está fechada.")
    except socket.error as e:
        print(f"Erro ao conectar-se à porta {port}: {e}")
    except socket.timeout:
        print(f"Tempo limite de conexão excedido para a porta {port}")

if __name__ == "__main__":
    host = input("Digite o site a ser escaneado (ex: facebook.com): ")
    ports = [21, 22, 23, 80, 443, 8080]
    for port in ports:
        scan_port(host, port)

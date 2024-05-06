import socket

ports = [21, 22, 23, 80, 3445, 443, 3307, 8080]
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    resposta = client.connect_ex(("facebook.com", port))
    client.close()
    if(resposta == 0):
        print(port, "aberta")
        
    else:   
        print(port, "Fechada")
        
        
    
    
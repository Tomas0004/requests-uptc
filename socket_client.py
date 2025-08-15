import socket
import ssl
import re

HOST = "132.255.20.44"
PORT = 443

context = ssl.create_default_context()

try: 
    with socket.create_connection((HOST, PORT)) as s:
            with context.wrap_socket(s, server_hostname="auth.uptc.edu.co") as ssls:
                print(f"SSL/TLS version: {ssls.version()}")
                ssls.sendall(b"POST /auth/realms/UPTC/login-actions/authenticate?client_id=SiWebDocente-publico&tab_id=A8ZDR7eu2VU HTTP/1.1\r\nHost: auth.uptc.edu.co\r\nCookie: AUTH_SESSION_ID=67283af0-acae-4f03-a2d5-212996fea490.auth.uptc.edu.co; AUTH_SESSION_ID_LEGACY=67283af0-acae-4f03-a2d5-212996fea490.auth.uptc.edu.co; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNzlhOWJiOS1jYTQwLTRkMDEtYWQ0YS0wZmQzY2UwOWNhYmIifQ.eyJjaWQiOiJTaVdlYkVzdHVkaWFudGUtcHVibGljbyIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vYXBwczMudXB0Yy5lZHUuY28vU2lXZWJFc3R1ZGlhbnRlRnJvbnRFbmQvIy9pbmljaW8vbWFpbiIsImFjdCI6IkFVVEhFTlRJQ0FURSIsIm5vdGVzIjp7InNjb3BlIjoib3BlbmlkIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnVwdGMuZWR1LmNvL2F1dGgvcmVhbG1zL1VQVEMiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vYXBwczMudXB0Yy5lZHUuY28vU2lXZWJFc3R1ZGlhbnRlRnJvbnRFbmQvIy9pbmljaW8vbWFpbiIsInN0YXRlIjoiYTZkMjQ0MGMtOWFiOC00MzY0LThjNTAtMDJjMjNmMzE4ZWU4Iiwibm9uY2UiOiJjMTRlZmQ2YS1mNjhkLTQ1ZTEtODVhZi1hNWNiZjllZDVkNmYiLCJyZXNwb25zZV9tb2RlIjoiZnJhZ21lbnQifX0.Z5RUg97Jm-3pdPEnbq22pudFnz1CF5ema_ClCmVw2N0; _ga_8H3Z256MX0=GS2.1.s1753754640$o5$g1$t1753755256$j60$l0$h0; _ga=GA1.3.262470619.1753329446; _gid=GA1.3.351536180.1753644303\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 29\r\nOrigin: null\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nPriority: u=0, i\r\nTe: trailers\r\nConnection: keep-alive\r\n\r\nusername=admin&password=fadas")
                data = ssls.recv(4096)
                print(f"Received {data.decode()}")
except ssl.SSLError as e:
    print(f"SSL Error: {e}")
except socket.error as e:
    print(f"Socket Error: {e}")
    
    
    

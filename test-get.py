import socket
import ssl

HOST = "132.255.20.44"
PORT = 443

context = ssl.create_default_context()

try: 
    with socket.create_connection((HOST, PORT)) as s:
            with context.wrap_socket(s, server_hostname="auth.uptc.edu.co") as ssls:
                print(f"SSL/TLS version: {ssls.version()}")
                ssls.send(b"GET /auth/realms/UPTC/login-actions/authenticate?execution=c7eb5254-826d-4fd8-87b7-74e09e5bd24b&client_id=SiWebDocente-publico&tab_id=Y-cnIlS-FRQ HTTP/1.1\r\nHost: auth.uptc.edu.co\r\nCookie: AUTH_SESSION_ID=75c96cc9-fb22-4541-90dd-2acb4e4111b2.auth.uptc.edu.co; AUTH_SESSION_ID_LEGACY=75c96cc9-fb22-4541-90dd-2acb4e4111b2.auth.uptc.edu.co; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNzlhOWJiOS1jYTQwLTRkMDEtYWQ0YS0wZmQzY2UwOWNhYmIifQ.eyJjaWQiOiJTaVdlYkRvY2VudGUtcHVibGljbyIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vYXBwczMudXB0Yy5lZHUuY28vU2lXZWJEb2NlbnRlRnJvbnRFbmQvIy8iLCJhY3QiOiJBVVRIRU5USUNBVEUiLCJub3RlcyI6eyJzY29wZSI6Im9wZW5pZCIsImlzcyI6Imh0dHBzOi8vYXV0aC51cHRjLmVkdS5jby9hdXRoL3JlYWxtcy9VUFRDIiwicmVzcG9uc2VfdHlwZSI6ImNvZGUiLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FwcHMzLnVwdGMuZWR1LmNvL1NpV2ViRG9jZW50ZUZyb250RW5kLyMvIiwic3RhdGUiOiJmMjhmOTIwOS04NjFkLTRmMTctYTBiNC1kZmZmNzI4YmIzMjMiLCJub25jZSI6IjVkNWI2YzAzLTUxYjEtNGMwMy1iZmY5LTZmNTQwYTE4OGNhZiIsInJlc3BvbnNlX21vZGUiOiJmcmFnbWVudCJ9fQ.3LIQXYPix_25VI4PNbfPgmq7U-Zg_bQ4VBwEQ3878-8; _ga=GA1.3.1297064787.1724681980; _ga_59DQSQQETS=GS1.1.1742867683.2.1.1742867704.0.0.0; _gid=GA1.3.841211510.1753815683\r\nCache-Control: max-age=0\r\nSec-Ch-Ua: \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"\r\nSec-Ch-Ua-Mobile: ?0\r\nSec-Ch-Ua-Platform: \"Linux\"\r\nAccept-Language: en-US,en;q=0.9\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nSec-Fetch-Site: same-site\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nReferer: https://apps3.uptc.edu.co/\r\nAccept-Encoding: gzip, deflate, br\r\nPriority: u=0, i\r\nConnection: keep-alive\r\nOrigin: null\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=jesus.suarez03&password=prMAs%23*%2F4789")
                data = ssls.recv(10000)
                print("\nReceived: ", data.decode())
                ssls.send(b"GET /auth/realms/UPTC/login-actions/authenticate?execution=c7eb5254-826d-4fd8-87b7-74e09e5bd24b&client_id=SiWebDocente-publico&tab_id=Y-cnIlS-FRQ HTTP/1.1\r\nHost: auth.uptc.edu.co\r\nCookie: AUTH_SESSION_ID=75c96cc9-fb22-4541-90dd-2acb4e4111b2.auth.uptc.edu.co; AUTH_SESSION_ID_LEGACY=75c96cc9-fb22-4541-90dd-2acb4e4111b2.auth.uptc.edu.co; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNzlhOWJiOS1jYTQwLTRkMDEtYWQ0YS0wZmQzY2UwOWNhYmIifQ.eyJjaWQiOiJTaVdlYkRvY2VudGUtcHVibGljbyIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vYXBwczMudXB0Yy5lZHUuY28vU2lXZWJEb2NlbnRlRnJvbnRFbmQvIy8iLCJhY3QiOiJBVVRIRU5USUNBVEUiLCJub3RlcyI6eyJzY29wZSI6Im9wZW5pZCIsImlzcyI6Imh0dHBzOi8vYXV0aC51cHRjLmVkdS5jby9hdXRoL3JlYWxtcy9VUFRDIiwicmVzcG9uc2VfdHlwZSI6ImNvZGUiLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FwcHMzLnVwdGMuZWR1LmNvL1NpV2ViRG9jZW50ZUZyb250RW5kLyMvIiwic3RhdGUiOiJmMjhmOTIwOS04NjFkLTRmMTctYTBiNC1kZmZmNzI4YmIzMjMiLCJub25jZSI6IjVkNWI2YzAzLTUxYjEtNGMwMy1iZmY5LTZmNTQwYTE4OGNhZiIsInJlc3BvbnNlX21vZGUiOiJmcmFnbWVudCJ9fQ.3LIQXYPix_25VI4PNbfPgmq7U-Zg_bQ4VBwEQ3878-8; _ga=GA1.3.1297064787.1724681980; _ga_59DQSQQETS=GS1.1.1742867683.2.1.1742867704.0.0.0; _gid=GA1.3.841211510.1753815683\r\nCache-Control: max-age=0\r\nSec-Ch-Ua: \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"\r\nSec-Ch-Ua-Mobile: ?0\r\nSec-Ch-Ua-Platform: \"Linux\"\r\nAccept-Language: en-US,en;q=0.9\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nSec-Fetch-Site: same-site\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nReferer: https://apps3.uptc.edu.co/\r\nAccept-Encoding: gzip, deflate, br\r\nPriority: u=0, i\r\nConnection: keep-alive\r\nOrigin: null\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 49\r\n\r\nusername=jesus.suarez03&password=prMAs%23*%2F4789")
                data = ssls.recv(10000)
                print("\nReceived: ", data.decode())
                
except ssl.SSLError as e:
    print(f"SSL Error: {e}")
except socket.error as e:
    print(f"Socket Error: {e}")
    
    
    

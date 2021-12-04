import socket 
import json

def runClient():
    host = socket.gethostname()
    port = 7439

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))

    message = {"query":"egg"}
    request = json.dumps(message)

    c.send(request.encode("utf-8"))
    response = c.recv(8192).decode("utf-8")

    jsonresponse = json.loads(response)
    print(jsonresponse)

    c.close()

if __name__ == '__main__':
    runClient()


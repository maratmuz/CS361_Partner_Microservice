#
#   Receiver runs first and stays running until it receives
#   a message. It connects to the socket and waits.
#   Once a message is received, it prints it,
#   sends a success message back to the sender, and then
#   breaks.
#

import time
import zmq
import http.client

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print(f"Receiver running")

# Runs and waits for a message
while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Message Received!: ")
    print(str(message, "utf-8"))
    time.sleep(1)

    #  Send reply back to client and break
    if message != "":
        conn = http.client.HTTPConnection("data.fixer.io")
        convert_to = "EUR"
        url = "/api/latest?access_key=c1ac9ab43f880df6293265dd830e85fb&symbols=" + convert_to
        payload = ""
        headers = {}

        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        socket.send(b"SUCCESS")
        break

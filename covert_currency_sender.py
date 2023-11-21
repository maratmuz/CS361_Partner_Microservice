import zmq
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 pipeline…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Sends a message
print(f"Sending message…")
message = "{USD, EUR, 10000}"
socket.send_string(message)

#  Get the reply.
time.sleep(1)
result = socket.recv()
print(f"Result: " + str(result))

time.sleep(1)
print(f"Sending message…")
message = "END"
socket.send_string(message)

time.sleep(1)
result = socket.recv()
print(f"Result: " + str(result))


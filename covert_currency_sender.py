import zmq

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
result = socket.recv()
print(f"Result: " + str(result))


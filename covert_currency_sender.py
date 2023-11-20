#
#   The sender runs once, connects to the socket,
#   sends a message through the pipeline
#   to the receiver, and then receives a success message.
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 pipeline…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Sends a message
print(f"Sending message…")
message = "{USD, EUR, 10000}"
socket.send(message)

#  Get the reply.
message = socket.recv()
print(f"Message: " + str(message, "utf-8"))

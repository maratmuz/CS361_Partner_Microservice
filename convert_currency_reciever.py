import json
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
    message = str(message)
    print(f"Message Received!: ", message)
    time.sleep(1)

    #  Send reply back to client and break
    if message != "":
        for i in range(len(message)):
            if message[i] == '{':
                convert_from = message[i + 1] + message[i + 2] + message[i + 3]
                convert_to = message[i + 6] + message[i + 7] + message[i + 8]
                amount = ""
                for i in range(13, len(message) - 2):
                    amount += message[i]

        conn = http.client.HTTPConnection("data.fixer.io")
        currency = convert_from
        url = "/api/latest?access_key=c1ac9ab43f880df6293265dd830e85fb&symbols=" + currency
        payload = ""
        headers = {}

        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        conversion = json.loads(data.decode("utf-8"))
        success = conversion["success"]

        if success == "fail":
            socket.send(b"FAIL")
        else:
            print(data)
            date = conversion["date"]
            rates = conversion["rates"]
            conversion_rates = rates[currency]

            conn = http.client.HTTPConnection("data.fixer.io")
            currency = convert_to
            url = "/api/latest?access_key=c1ac9ab43f880df6293265dd830e85fb&symbols=" + currency
            payload = ""
            headers = {}

            conn.request("GET", url, payload, headers)
            res = conn.getresponse()
            data = res.read()
            conversion = json.loads(data.decode("utf-8"))
            success = conversion["success"]

            if success == "fail":
                socket.send(b"FAIL")
            else:
                print(data)
                date = conversion["date"]
                rates = conversion["rates"]
                total = rates[currency]

                result = float(total)/float(conversion_rates)
                result *= float(amount)
                round(result, 2)

                result_msg = "{Date: " + date + ", Convert From: " + convert_from + ", Convert To: " + convert_to + ", Total Amount: " + str(amount) + ", Result: " + str(result)
                print(result_msg)

                socket.send_string(result_msg)
        break


# CS361_Partner_Microservice
Microservice for my partner in CS361

The microservice is stored in "convert_currency_reciever.py". It must be run first and it runs indefinitely, waiting for a message to be sent. 

Then the sender uses the socket 5555 to send a message using socket.send_string() in this format: "{*currency converting from(in 3 letters)*, *currency converting to(in 3 letters)*, *amount being converted*}
e.g. "USD, JPY, 10000"

After the microservice receives the message, it uses an API from fixer.io to convert the currency. However, due to the free service having many restrictions, it will only allow me to convert from EUR.

What the microservice does to get around this is to first convert 1 EUR to the currency we are converting from.

Then it converts 1 EUR to what we are converting to.

Then it divides these amounts e.g. : "1 EUR = 2 USD" -> "1 EUR = 20 JPY" -> "1 USD = 10 JPY"

Once it has this value, it multiplies it by the amount being converted e.g. "20 * 10000 = 200000"

Finally, it sends a message back in this format: "{*Date of conversion*, *currency converting from(in 3 letters)*, *currency converting to(in 3 letters)*,  *amount being converted*, *resulting conversion*}

At any point during conversion, if the API fails, the message sent back will instead be "FAIL"

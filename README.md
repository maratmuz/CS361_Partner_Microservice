# CS361_Partner_Microservice
Microservice for my partner in CS361

The microservice is stored in "convert_currency_reciever.py". "convert_currency_sender.py" goes into the main file to access the microservice. 

# Sender Message to Receiver:
When the sender is run, it first runs the receiver as well, ensures the receiver exists, and then connects them to the same socket.

The sender uses socket 5555 to send a message using socket.send_string() in this format: "{*currency converting from(in 3 letters)*, *currency converting to(in 3 letters)*, *amount being converted*}
e.g. "USD, JPY, 10000"

# How the microservice receiver works
After the microservice receives the message, it uses an API from fixer.io to convert the currency. However, due to the free service having many restrictions, it will only allow me to convert from EUR.

To get around this, the microservice first converts 1 EUR to the currency we are converting from.

Then it converts 1 EUR to what we are converting to.

Then it divides these amounts e.g. : "1 EUR = 2 USD" -> "1 EUR = 20 JPY" -> 20/2 = 10 -> "1 USD = 10 JPY"

Once it has this value, it multiplies it by the amount being converted e.g. "20 * 10000 = 200000"

# Receiver Message back:
Finally, it sends a message back in this format: "{*Date of conversion*, *currency converting from(in 3 letters)*, *currency converting to(in 3 letters)*,  *amount being converted*, *resulting conversion*}
e.g. "11/20/2023, USD, JPY, 10000, 200000"

At any point during conversion, if the API fails, the message sent back will instead be "FAIL"

# Ending the while loop:
If the sender sends the message "End" it will stop the receiver loop. The sender file currently automatically does this with a function.

# UML sequence diagram
![image](https://github.com/maratmuz/CS361_Partner_Microservice/assets/123781512/38521e15-2e68-422b-bbf5-5b4e57df033a)


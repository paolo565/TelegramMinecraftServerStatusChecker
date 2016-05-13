## TelegramMinecraftServerStatusChecker
This bot sends you a message on telegram when your minecraft server goes down or when the latency exceeds the limit.

### Installation
Python:

    $ pip install -r requirements.txt
Python 3:

    $ pip3 install -r requirements.txt

### Creating the telegram bot
You can find all the information to create a new telegram bot here: https://core.telegram.org/bots#6-botfather

### Getting the chat id
If you don't know the id of your chat you can send a message to the bot, open the following url: ``https://api.telegram.org/bot<YourBotToken>/getUpdates`` and copy the number after ``"chat":{"id":``

### Configuration
Create a file called ``config.py``
```python
MAX_LATENCY = 200
CHECK_DELAY = 10
SERVER_IP = "YOUR-SERVER-IP"
COMPUTER_NAME = "NAME-DISPLAYED-BY-THE-BOT"

TELEGRAM_CHAT_ID = 0 # The id of your telegram chat
TELEGRAM_TOKEN = "YOUR-TELEGRAM-API-KEY"
```
import telegram

class TelegramModel():
    
    def __init__(self):
        self.chat_token = "2099015091:AAHFrqoe7ezCRHkLSB63cQ34ATn04Xn82-s"
        self.bot = telegram.Bot(token = self.chat_token)
    
    def get_userupdate(self):
        updates = self.bot.getUpdates()
        user_set = set()
        for u in updates:
            user_set.add(u.message['chat']['id'])
            self.user_lst = list(user_set)

    def send_message(self,text):
        self.get_userupdate()
        for usr in self.user_lst:
            self.bot.sendMessage(chat_id = usr, text=text)



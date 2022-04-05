import ampalibe
from conf import Configuration

bot = ampalibe.init(Configuration())
chat = bot.chat

class UserView:
    
    def greeting(self, sender_id):
        chat.send_message(sender_id, "Hello, Ampalibe")

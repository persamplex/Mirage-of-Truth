import telepot
from telepot.loop import MessageLoop
import time


TOKEN = "7556280736:AAEsBVYsPQV816UZLtxAHhSMLeLF5-n2Zko"

def handle(msg):
    chat_id = msg['chat']['id'] 
    text = msg.get('text', '')

    bot.sendMessage(chat_id, f"شما گفتید: {text}\nچت ایدی: `{chat_id}`",parse_mode="MarkDown")

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()


while True:
    time.sleep(10)

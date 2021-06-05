from telethon import TelegramClient, sync
import random, re, time
import wish

def message(internal_compliments, internal_api_id, internal_api_hash): 
    internal_client = TelegramClient('Compliments', internal_api_id, internal_api_hash) 
    internal_client.start()  
    rand_compl = random.choice(
        internal_compliments)  
    internal_client.send_message('+77081875539', rand_compl)  
    internal_client.disconnect()  
    print('ОТПРАВЛЕНО ПОЖЕЛАНИЕ: ' + str(rand_compl))  




api_id = 4023803
api_hash = '160ab43b23945ec7fdfdb1d8ed40838c'
wish = wish.parse()

while True:
	message(wish, api_id, api_hash)
	time.sleep(600)
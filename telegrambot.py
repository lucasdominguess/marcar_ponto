import telebot
import logging
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
keyApi = os.getenv('API_TOKEN')
chat_id = os.getenv('CHAT_ID')

#criar bot no telegram via botFather 
# os.getenv('API_TOKEN')
# keyApi = '7820682159:AAEXo2KxfB7D5o0UQKuqy1qklorpX-s-zDc' #token gerado na criação do bot
# chat_id ="@rotina_ponto_g4f"   #id do chat/grupo  

# Diretório base e arquivo de log
base_dir = Path(__file__).resolve().parent
logging_file = base_dir / 'logging.log'

class TelegramBot:
    def __init__(self):
        # Configurando o logging
        logging.basicConfig(filename=logging_file,level=logging.INFO,format='%(asctime)s -  %(levelname)s  - %(message)s')

        self.bot = telebot.TeleBot(keyApi)
        # logging.info('Bot inicializado')

    def send_message(self,msg: str):
        
        try:
            self.bot.send_message(chat_id, msg)
            logging.info('Mensagem via telegram enviada com sucesso')
        except Exception as e:
            logging.error(f'Erro ao enviar mensagem via Telegram: {e}')
        

if __name__ == "__main__":
    
    bot = TelegramBot()
    bot.send_message('Hello, this is a test!')

import requests
import time
# import logging
import random
from datetime import date
import re
from calendra.america import Brazil
from email_ponto import EmailLogging
from pathlib import Path
from telegrambot import TelegramBot
import os
# from dotenv import load_dotenv
from log_config import setup_logging

# load_dotenv()
logging=setup_logging("main")

# user= os.getenv("USER")
# password = os.getenv("PASSWORD")
# email_suffix = os.getenv("EMAILSUFFIX")
user= ''
password =''
email_suffix = ''

# base_dir = Path(__file__).resolve().parent
# logging_file = base_dir / 'logging.log'

# chat_id = "@rotina_ponto_g4f"

class BatidaPonto():
    def __init__(self,*args):
        # logging.basicConfig(filename=logging_file, level=logging.INFO, format='%(asctime)s -  %(levelname)s  - %(message)s')
        self.s = requests.Session()
        Br = Brazil()
        work_day = Br.is_working_day(date.today())
        login = {
            'user': user,
            'password': password,
            'expirationRememberMe': -1,
            'emailSuffix': email_suffix
        }
        if work_day:
            logging.warning("Dia de Trabalho")

            # r = self.s.post('https://platform.senior.com.br/auth/LoginServlet', data=login)

            # print(r)
            # logging.info(f'Resultado da primeira request {r}')

        #     all_cookies = self.s.cookies.get_dict()
        #     token = all_cookies['com.senior.token']
        #     token = token[token.find('access_token') + 21:token.find('refresh_token') - 9]
        #     self.headers = {
        #      "Content-Type": 'application/json',
        #      "Authorization": "",
        #      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        #     }
        #     self.headers['Authorization'] = f"bearer {token}"
            self.Ponto()
        # else:
        #     EmailLogging("Final de semana ou Feriado")
        #     logging.warning("Final de semana ou Feriado")


    def Ponto(self):
        print('iniciando')
        logging.info('Iniciando')
       #num = random.randint(0,2)
        num = random.randint(10,20)  
        mult = random.randint(1,3)
        ale = int(num*mult)
        # time.sleep(ale)
        # print(f'Numero aleatorio gerado'ale)
        # print(f"Numero entre 10 e 20 foi : {num},e foi multiplicado por {mult}")
        # print(f"Numero aleatorio gerado: {ale}")
        # time.sleep(ale)
        try:
            print('Iniciando ..')
            # dados_batida = {"clockingInfo":
            #                 {"company":{"id":"541c4dca-28f5-4c1c-9e92-fa5b85baf4c9","arpId":"fcd93fc5-eabc-47d8-81d4-405685ac8094","identifier":"07094346000145","caepf":"0","cnoNumber":"0"},
            #                  "employee":{"id":"b2972e46-2f4b-461b-bf0e-cbdb2640a05e","arpId":"7c9a51e6-0396-4608-b58d-e88ef4d4c0de","cpf":"41487305869","pis":"16519832724"},"appVersion":"3.11.0","timeZone":"America/Sao_Paulo",
            #                  "signature":{"signatureVersion":1,"signature":"MWEzMzZmYTU5YjI5M2QxNzI0MGI4NDg4ZWZlNjhhZjRiMWM1NmJhMmRjY2RlNzk0YWFmMDI5ZWY1N2ZlZmE0MA=="},"use":"02"}}

            # r = self.s.post('https://platform.senior.com.br/t/senior.com.br/bridge/1.0/rest/hcm/pontomobile_clocking_event/actions/clockingEventImportByBrowser', 
            #         json=dados_batida, headers=self.headers)
            
            # logging.info(f'Resultado da segunda request {r}')

            # data = r.json()

            # date_event = data['clockingResult']['clockingEventImported']['dateEvent']
            # time_event = data['clockingResult']['clockingEventImported']['timeEvent']

            # # logging.warning(r)
            # logging.info(r.json())
           
            bot = TelegramBot()
            # bot.send_message(chat_id,f'Marcação de ponto realizada com sucesso Data: {date_event} - Hora: {time_event} ')
            bot.send_message(f'Marcação de ponto realizada com sucesso ')

            # EmailLogging(f'Marcação de ponto realizada com sucesso Data: {date_event} - Hora: {time_event}')
            # logging.info(f'Marcação de ponto realizada com sucesso Data: {date_event} - Hora: {time_event}')
            # EmailLogging(f'Marcação de ponto realizada com sucesso ')
            print('finalizado')
        except TypeError as err:

            bot.send_message(f'Erro ao marcar ponto {err}')
            # EmailLogging(f'Erro ao marcar ponto {err}')
            logging.error(f'{err}')
        finally:
            logging.warning("FINALIZADO")

if __name__ == '__main__':
    BatidaPonto()
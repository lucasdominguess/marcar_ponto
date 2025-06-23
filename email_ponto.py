import os
import logging 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# se prodam mudar para true se nox false
# EMAIL_IS_PRODAM = True

# SMTP_SERVER_NOX = 'smtp.email.sa-saopaulo-1.oci.oraclecloud.com'
# SMTP_PORT_NOX = 587
# SMTP_USERNAME_NOX = 'ocid1.user.oc1..aaaaaaaan43kkrz5frw6cwd555mulm7v6ylztb2xmasnnzpcw7be3nrnj34a@ocid1.tenancy.oc1..aaaaaaaai7a72s5jgxce6rik7qna2nx2j3flclxvvrkg3mojvxmrjz3hmf6q.jo.com'
# SMTP_PASSWORD_NOX = 'MkVFPT-w4(3(xuy_2J9r'


# SMTP_SERVER_PRODAM = 'SMTPCORP.PRODAM'
# SMTP_PORT_PRODAM = 25 # Porta do servidor SMTP (normalmente 587 para TLS ou 465 para SSL)

EMAIL_IS_PRODAM = False

SMTP_SERVER_NOX = 'smtp.email.sa-saopaulo-1.oci.oraclecloud.com'
SMTP_PORT_NOX = 587
SMTP_USERNAME_NOX = 'ocid1.user.oc1..aaaaaaaamgxkl4xjqwnxmjsntrujbwxae7xo7zor4hnxqp2ssi6yzfvlfzbq@ocid1.tenancy.oc1..aaaaaaaai7a72s5jgxce6rik7qna2nx2j3flclxvvrkg3mojvxmrjz3hmf6q.pw.com'
SMTP_PASSWORD_NOX = '[;j9DIBcoC]6r0T:P1kE'


SMTP_SERVER_PRODAM = 'SMTPCORP.PRODAM'
SMTP_PORT_PRODAM = 25 # Porta do servidor SMTP (normalmente 587 para TLS ou 465 para SSL)



class EmailLogging:
    def __init__(self, msg):
        self.email_is_prodam = EMAIL_IS_PRODAM
        self.smtp_server_nox = SMTP_SERVER_NOX 
        self.smtp_port_nox = SMTP_PORT_NOX
        self.smtp_username_nox = SMTP_USERNAME_NOX
        self.smtp_password_nox = SMTP_PASSWORD_NOX

        self.smtp_server_prodam = SMTP_SERVER_PRODAM
        self.smtp_port_prodam = SMTP_PORT_PRODAM

        self.mensagem = msg
        self.run()
    
    def email(self):
        # Prodam
        if self.email_is_prodam:
            server = smtplib.SMTP(self.smtp_server_prodam, self.smtp_port_prodam)
            sender = 'smsdtic@prefeitura.sp.gov.br'
            
        # NoxTec
        else:
            sender  = 'oci@smsprefeiturasp.org'
            server = smtplib.SMTP(self.smtp_server_nox, self.smtp_port_nox)


        try:
            recipients = ['lucasdomingues25.dev@gmail.com']
            msg = MIMEText(self.mensagem)
            msg['Subject'] = "Rotina Ponto"
            msg['From'] = sender
            msg['To'] = ", ".join(recipients)
            server.starttls()  # Iniciar TLS (Transport Layer Security) para segurança
            server.login(self.smtp_username_nox, self.smtp_password_nox)
            server.sendmail(sender, recipients, msg.as_string())

        except Exception as e:
            logging.error(f'Erro ao enviar o email {e}')

        finally:
            server.quit()


    def run(self):
        self.email()


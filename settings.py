import os
from dotenv import load_dotenv

load_dotenv()

mail_adress = 'sea-of-max@yandex.ru'
mail_pass = os.getenv("PASSWORD_YA")

base_url = 'https://uts.sirius.online//#/auth/register/qainternship'
import os
from dotenv import load_dotenv
load_dotenv()


class DataLogin:

    base_url = 'https://uts.sirius.online//#/auth/register/qainternship'
    mail_address = 'sea-of-max@yandex.ru'
    mail_pass = os.getenv("PASSWORD_YA")
    vosh_login = 'v00.000.000'
    name = 'Макс'
    surmane = 'Хор'
    fathersname = 'Ген'

    d_o_birth = '12.12.1988'
    phone_numb = '123456789'
    snils = '16675209900'
    profesion = 'СуперМарио'
    city = 'Астана'
    comp_name = 'йцукенгш'
    school = 'йцукенгш456'
    grade = '5Ю'


class WrongDataLogin:

    mail_address = '456@9.ro'
    vosh_loginzero = '00.000.000'
    vosh_loginlatin = 'vdf.weq.mnb'
    namelatin = 'qwertyuiopasdfghjklzxcvbnm'
    namecyrillic = 'цукенгшщзхъфывапролджэячсмитьбю'
    name260 = 'Жора'*65
    namespec = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
    surmane = ''
    fathersname = ''

    d_o_birth = '00.00.1000'
    phone_13dig = '+79346784562163'
    snils = '000000000000'
    profesion = ''
    city = '23456789'
    comp_namespec = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
    school = ''
    grade = ''

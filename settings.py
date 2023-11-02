import os
from dotenv import load_dotenv
load_dotenv()


class DataLogin:

    base_url = 'https://uts.sirius.online//#/auth/register/qainternship'
    mail_address = 'sea-of-max@yandex.ru'
    mail_pass = os.getenv("PASSWORD_YA")
    vosh_login = ''
    name = ''
    surmane = ''
    fathersname = ''

    d_o_birth = '12.12.1988'
    phone_numb = ''
    snils = ''
    profesion = ''
    city = ''
    comp_name = ''
    school = ''
    grade = ''


class WrongDataLogin:

    mail_address = '456@9.ro'
    mail_pass = ''
    vosh_loginzero = 'v00.000.000'
    vosh_loginlatin = 'vdf.weq.mnb'
    namelatin = 'qwertyuiopasdfghjklzxcvbnm'
    namecyrillic = 'цукенгшщзхъфывапролджэячсмитьбю'
    name260 = 'Жора'*65
    namespec = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
    surmane = ''
    fathersname = ''

    d_o_birth = ''
    phone_13dig = '+79346784562163'
    snils = ''
    profesion = ''
    city = ''
    comp_namespec = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
    school = ''
    grade = ''

print(WrongDataLogin.name260)
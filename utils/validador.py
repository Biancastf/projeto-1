import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_cep(cep):
    padrao = r'^\d{5}-\d{3}$'
    return re.match(padrao, cep) is not None

def validar_senha(senha):
    if len(senha) < 6:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'\d', senha):
        return False
    return True


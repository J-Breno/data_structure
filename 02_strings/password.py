import re

def validar_senha(senha):
    if (len(senha) >= 8 and
        re.search(r"\d", senha) and
        re.search(r"[A-Za-z]", senha) and
        re.search(r"[@#&]", senha)):
        print("VÁLIDA")
    else:
        print("INVÁLIDA")

validar_senha("amrca154682")
validar_senha("amrca154682@")
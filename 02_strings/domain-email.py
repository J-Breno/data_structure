def extract_email_information(email):
    usuario = ""
    dominio = ""
    brasileiro = False

    email = email.split("@")
    usuario = email[0]
    dominio = email[1]

    if ".br" in dominio:
        brasileiro = True

    print("Usuario: ", usuario)
    print("Dominio: ", dominio)
    print("Brasileiro: ", brasileiro)

extract_email_information("joao.silva23@yahoo.com.br")
print()
extract_email_information("maria123@gmail.com")
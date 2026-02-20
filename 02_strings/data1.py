def extract_date_data(date):
    date = date.split("/")
    dia = date[0]
    mes = date[1]
    ano = date[2]

    if dia.startswith("0"):
        dia = dia.replace("0", "")

    if mes.startswith("0"):
        mes = mes.replace("0", "")

    print("Dia:", dia)
    print("Mes:", mes)
    print("Ano:", ano)

extract_date_data("21/07/2010")
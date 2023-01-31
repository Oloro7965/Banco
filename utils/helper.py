from datetime import date,datetime

def date_string(Data:date):
    return Data.strftime('%d/%m/%Y')
def string_date(data:str):
    return datetime.strptime(data,'%d/%m/%Y')
def Moeda_formatada(valor:float)->str:
    return f'R$ {valor:,.2f}'
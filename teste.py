# from datetime import date,datetime
# print(date.today())
# a=date.today()
# print(a.strftime('%d/%m/%Y'))
# # data=input('digite a data ')
# # a_conv=datetime.strptime(data,'%d/%m/%Y')
# # print(a_conv.strftime('%d/%m/%Y'))
# valor=float(input('digite o valor '))
# print(f'R${valor:,.2f}')
import models.client
cliente1=models.client.Cliente('Pedro','pedroromulo@hotmail.com','06676755580','26/02/1997')
print(cliente1.nome)

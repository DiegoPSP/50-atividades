from datetime import datetime
localizar = datetime.fromisocalendar(2002, 36, 1) #Retorna um datetime correspondente à data no calendário ISO especificada por year, week e day.
busca = datetime(2002, 9, 2)
print(f"{localizar}\n{busca.isocalendar()}")#.isocalendar()Retorna um objeto tupla nomeada com três componentes: year, week e weekday.
#Não consegui fazer a chamada do comando .isoformat() na variável "busca", pois já fiz a chamada acima e não deu pra formatar.

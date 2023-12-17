lista = ['maçã', 'maçã', 'uva',  'banana', 'uva', 'maçã']
lista_sem_duplicatas = []

lista_sem_duplicatas = list(set(lista))#list força a ser do tipo lista e não perde a ordem
print(f"Lista original:{lista}")
lista = lista_sem_duplicatas
print(f"Lista após a alteração: {lista}")

 
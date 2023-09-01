lista_compras = [
    
]
itens_removidos = [

]
while True:
    itens= input('Adicione itens a lista  (ou FIM para encerrar)  ').lower()
    if itens== 'fim':
        break
    else:
        lista_compras.append(itens)
        
print (lista_compras)

while True:
    remover= input('Escolha um item para remover( ou digite FIM para encerrar)  ').lower()
    if remover== 'fim':
        break
    else:
        lista_compras.remove(remover)
        itens_removidos.append(remover)
print (lista_compras)
print (itens_removidos)
    
ordenar = input('Deseja exibir a lista de compras em ordem alfabética? (SIM/NÃO): ')
if ordenar.lower() == "SIM":
    lista_compras.sort
print (f'Lista de compras: {lista_compras}')
print (f'Sua lista de compras tem {len(lista_compras)} itens')

apagar = input ('Você deseja apagar a lista? (sim/não) ')
lista_reserva = lista_compras.copy()
print (f'Sua lista de compras tem {len(lista_compras)} itens')
if apagar == 'sim':
 print (lista_reserva)
exluir = input('Você tem certeza que quer excluir todos os itens da lista? (Sim/não)') 
if exluir == 'sim':
    lista_compras.clear()
    print (f'Sua lista de compras tem {len(lista_compras)} itens')
else:
    print ('Sua lista não será apagada')   
recuperar = input( 'Deseja recuperar os itens da lista?(sim/não)  ')    
if recuperar == "sim":
    lista_compras.extend(lista_reserva)
    print ("Sua Lista de compras foi recuperada com sucesso!")
    print(lista_compras)
    print (f'Sua lista de compras tem {len(lista_compras)} itens')
    
    
    

    
     
    
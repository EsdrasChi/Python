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
    
#Não entendi como usar as funções index e pop que foram solcitadas na atividade 3 da lista


    
     
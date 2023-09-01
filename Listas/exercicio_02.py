lista_compras = [
    
]
while True:
    itens= input('Deseja adicionar itens a lista?  (Para encerrar digite FIM)  ').lower()
    if itens== 'fim':
        break
    else:
        lista_compras.append(itens)
        
print (lista_compras)

while True:
    remover= input('Deseja remover intens da lista?(Para encerrar digite FIM)  ').lower()
    if remover== 'fim':
        break
    else:
        lista_compras.remove(remover)
print (lista_compras)
    



    
     
materiais_escritorio=['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clipsde Metal', 'Grampos', 'Post It', 'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']
print (f'materiais de escritório 2023')
for elemento in materiais_escritorio:
    print(elemento)

contagem_itens = len(set(materiais_escritorio))
print(f"Sua lista de compras tem {contagem_itens} itens.")

pergunta = input("Deseja verificar itens duplicados na lista? (Sim/não)")
if pergunta.lower() == "sim":
    itens_duplicados = []
for elemento in materiais_escritorio:
        if materiais_escritorio.count(elemento) > 1 and elemento not in itens_duplicados:
            itens_duplicados.append(elemento)
print ("\nITENS DUPLICADOS")    
for item in itens_duplicados:
     print(item)
quantidade_duplicados = len(itens_duplicados)
print(f"Quantida de itens duplicados: {quantidade_duplicados}.")
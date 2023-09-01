materiais_escritorio=['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clipsde Metal', 'Grampos', 'Post It', 'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']
print (f'materiais de escritório 2023')
for elemento in materiais_escritorio:
    print(elemento)

contagem_itens = len(set(materiais_escritorio))
print(f"Sua lista de compras tem {contagem_itens} itens.")
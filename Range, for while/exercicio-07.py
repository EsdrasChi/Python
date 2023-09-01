nota_1 = float (input('Digite a primeira nota: '))
nota_2 = float (input('Digite a segunda nota: '))
nota_final = nota_1+nota_2%2 
if nota_final >=7:
    print('Aprovado')
else: print('Reprovado')



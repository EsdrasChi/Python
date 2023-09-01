import os

lista_candidatos = [
  'tião do gás'
  'Zézinho 71'
  'Maria Marimar'
]

lista_votos = [
  
  0, #votos tião do gás
  0, #votos zezinho 71
  0  #votos MAria mariamar
]
lista_nb = [
  0,
  0,
]
turno = True
while turno:
  #controle do WHILE: se o quer for digitado for 'encerrar' o valor
  #da variavel 'turno' será alterado para falso
  print('Eleições Municiapais 2067')
  print('Cargo do pleito: Vereador municipal\n')
  print(f'[52] - TIÃO DO GÁS: {lista_votos[0]}')
  print(f'[71] - ZEZINHO 71:   {lista_votos[1]}')
  print(f'[98] - MARIA MARIMAR  {lista_votos[2]}')
  print(f'[0] - NULO {lista_nb[0]}')
  print(f'[1] - BRANCO {lista_nb[1]}')
  
  #f anota variavel dentro do print
  
  voto = input('Informe o número do seu candidato: ')
  os.system('cls')
  if voto == '52':
    lista_votos[0] = lista_votos[0]+1
  if voto == '71':
    lista_votos[1] = lista_votos[1]+1
  if voto == '98':
    lista_votos[2] = lista_votos[2]+1
  if voto == 'encerrar':
     turno = False
  if voto == '0':
   lista_nb[0] = lista_nb[0]+1 
  if voto == '1':
    lista_nb[1] = lista_nb[1]+1    
else:
  print(lista_votos)     
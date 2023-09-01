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
turno = True
while turno:
  #controle do WHILE: se o quer for digitado for 'encerrar' o valor
  #da variavel 'turno' será alterado para falso
  print('Eleições Municiapais 2067')
  print('Cargo do pleito: Vereador municipal\n')
  print('[52] - TIÃO DO GÁS')
  print('[71] - ZEZINHO 71')
  print('[98] - MARIA MARIMAR')
  print('[0] - NULO')
  print('[1] - BRANCO')
  
  voto = input('Informe o número do seu candidato: ')
  if voto == '52':
    lista_votos[0] = lista_votos[0]+1
  if voto == '71':
    lista_votos[1] = lista_votos[1]+1
  if voto == '98':
    lista_votos[2] = lista_votos[2]+1
  if voto == 'encerrar':
     turno = False
else:
  print(lista_votos)     
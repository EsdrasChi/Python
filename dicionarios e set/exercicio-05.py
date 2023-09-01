pessoas = {
  'nome': 'João', 
  'idade': '25',
   'cidade': 'Belo Horizonte'
}
print(pessoas['nome'])
if 'altura' in pessoas:
  print(pessoas.get('altura'))
else: 
  print('CHAVE NÃO EXISTE')

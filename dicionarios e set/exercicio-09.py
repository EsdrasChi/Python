pessoas = {
  'nome': 'João', 
  'idade': '25',
   'cidade': 'Belo Horizonte'
}

dados_pessoais= pessoas.items()
for dados in dados_pessoais:
    print(pessoas.get(dados[0]))

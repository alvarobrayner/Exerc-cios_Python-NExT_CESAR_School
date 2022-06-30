'''
PyFinanceiro

Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros chamado dados_financeiros.txt. O conjunto de dados é composto por duas colunas: Data e Lucros/Perdas, separados por virgula. (Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)

Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:
- O número total de meses incluídos no conjunto de dados
- O valor total líquido de "Lucros / Perdas" durante todo o período
- A média dos "Lucros / Perdas" durante todo o período
- A média das mudanças em "Lucros / Perdas" durante todo o período
- O maior aumento nos lucros (data e valor) durante todo o período
- A maior redução nas perdas (data e valor) ao longo de todo o período

Por exemplo, sua análise deve ser semelhante a esta abaixo:

Analise financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309,04
Variação da média: $ -2315,12
Maior aumento nos lucros: fevereiro de 2012 ($ 1926159)
Maior redução nos lucros: setembro de 2013 ($ -2196167)

Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto relatório.txt com os resultados.
'''

meses = []
lucros_perdas = []
mudancas = []

with open('dados_financeiro.txt', 'r') as arquivo:
  for mes in arquivo.readlines()[1:]:
    meses.append(mes.split(',')[0])
    lucros_perdas.append(int(mes.split(',')[1].replace('\n', '')))

# número total de meses
total_meses = len(meses)

# valor total líquido de "Lucros / Perdas"
valor_total = sum(lucros_perdas)

# média dos "Lucros / Perdas"
media = round(valor_total / total_meses, 2)

# média das mudanças em "Lucros / Perdas"
for n in range(total_meses):
  if n == 0:
    pass
  else:
    mud = lucros_perdas[n] - lucros_perdas[n - 1]
    mudancas.append(mud)

media_mudancas = round(sum(mudancas) / len(mudancas), 2)
mudancas.insert(0, 0)

# maior aumento nos lucros (data e valor)
maior_aumento = max(mudancas)
index_aumento = mudancas.index(maior_aumento)
mes_maior_aumento = meses[index_aumento]

# maior redução nas perdas (data e valor)
maior_reducao = min(mudancas)
index_reducao = mudancas.index(maior_reducao)
mes_maior_reducao = meses[index_reducao]

with open('relatório.txt', 'w') as arq_relatorio:
  arq_relatorio.write(f'Analise financeira\n{"-" * 28}\n')
  arq_relatorio.write(f'Total de meses: {total_meses}\n')
  arq_relatorio.write(f'Total: R$  {valor_total}\n')
  arq_relatorio.write(f'Média: R$ {media}\n')
  arq_relatorio.write(f'Variação da média: R$ {media_mudancas}\n')
  arq_relatorio.write(f'Maior aumento nos lucros: {mes_maior_aumento} (R${maior_aumento})\n')
  arq_relatorio.write(f'Maior redução nos lucros: {mes_maior_reducao} (R${maior_reducao})')
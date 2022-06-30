'''
PyVotação

Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)

Você receberá um conjunto de dados de enquete chamado dados_eleção.txt. O conjunto de dados é composto por três colunas: ID do eleitor,Município e Candidato. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:
- O número total de votos expressos
- Uma lista completa de candidatos que receberam votos
- A porcentagem de votos que cada candidato ganhou
- O número total de votos que cada candidato ganhou
- O vencedor da eleição com base no voto popular.

Por exemplo, sua análise deve ser semelhante a esta abaixo:

Resultados eleitorais
-------------------------
Total de votos: 3521001
-------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Vencedor: Khan
-------------------------

Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto resultado.txt com os resultados.
'''

from os import write
votos = []
nomes = []
vencedor = ''

with open('dados_elecao.txt', 'r') as arquivo:
  for candidato in arquivo.readlines()[1:]:
    votos.append(candidato.split(',')[2].replace('\n', ''))

# número total de votos
total_votos = len(votos)

# lista completa de candidatos que receberam votos
for nome in votos:
  if nome not in nomes:
    nomes.append(nome)

# O número total de votos que cada candidato ganhou
votos_khan = votos.count('Khan')
votos_correy = votos.count('Correy')
votos_li = votos.count('Li')
votos_otooley = votos.count("O'Tooley")

# porcentagem de votos que cada candidato
perc_khan = round((votos_khan / len(votos)) * 100, 2)
perc_correy = round((votos_correy / len(votos)) * 100, 2)
perc_li = round((votos_li / len(votos)) * 100, 2)
perc_otooley = round((votos_otooley / len(votos)) * 100, 2)

# vencedor da eleição
if perc_khan >= perc_correy and perc_khan >= perc_li and perc_khan >= perc_otooley:
  vencedor = 'Khan'
elif perc_correy >= perc_khan and perc_correy >= perc_li and perc_correy >= perc_otooley:
  vencedor = 'Correy'
elif perc_li >= perc_correy and perc_li >= perc_khan and perc_li >= perc_otooley:
  vencedor = 'Li'
else:
  vencedor = "'O'Tooley"

with open('resultado.txt', 'w') as arq_resultado:
  arq_resultado.write(f'Resultados eleitorais\n{"-" * 25}\n')
  arq_resultado.write(f'Total de votos: {total_votos}')
  arq_resultado.write(f'\n{"-" * 25}\n')
  arq_resultado.write(f'Khan: {perc_khan}% ({votos_khan})\n')
  arq_resultado.write(f'Correy: {perc_correy}% ({votos_correy})\n')
  arq_resultado.write(f'Li: {perc_li}% ({votos_li})\n')
  arq_resultado.write(f"O'Tooley: {perc_otooley}% ({votos_otooley})")
  arq_resultado.write(f'\n{"-" * 25}\n')
  arq_resultado.write(f'Vencedor: {vencedor}')
  arq_resultado.write(f'\n{"-" * 25}')
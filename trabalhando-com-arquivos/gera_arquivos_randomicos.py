import random
import string
from pathlib import Path

pasta_atual = Path(__file__).parent
formatos_de_arquivos = ['.py', '.pdf', '.txt', '.csv', '.xlsx', '.json', '.html']

def arquivo_randomico(quantidade):
    letters = string.ascii_lowercase
    arquivos = [''.join(random.choice(letters) for _ in range(random.randint(4, 8))) for _ in range(quantidade)]
    arquivos = [f'{nome}{formatos_de_arquivos[random.randint(0, len(formatos_de_arquivos) - 1)]}' for nome in arquivos]
    return arquivos

pasta_arquivos = pasta_atual / 'arquivos_desafios'

# Cria a pasta de arquivos se ela não existir
if not pasta_arquivos.exists():
    pasta_arquivos.mkdir()

# Cria pelo menos um arquivo de cada tipo
for formato in formatos_de_arquivos:
    nome_arquivo = f'arquivo_{random.randint(1, 100)}{formato}'
    with open(pasta_arquivos / nome_arquivo, 'w') as f:
        f.write(nome_arquivo)

# Cria mais 49 arquivos aleatórios
for arquivo in arquivo_randomico(49):
    nome_arquivo = f'arquivo_{random.randint(1, 100)}{arquivo[-4:]}'
    with open(pasta_arquivos / nome_arquivo, 'w') as f:
        f.write(nome_arquivo)

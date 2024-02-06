from pathlib import Path
import pandas as pd

#creating a path
path = Path(__file__).parent

#opening excel
clientsExcel = pd.read_excel(path / 'planilhas' / 'clientes.xlsx')
print(clientsExcel.head(10))
print('======================\n\n\n')
#opening a especific excel tab
specificTab = pd.read_excel(path / 'planilhas' / 'clientes.xlsx', sheet_name='SC')
print('specific tab')
print(f'{specificTab.head(10)}')
print('======================\n\n\n')
#removing header
print('removing header')
clientsExcel = pd.read_excel(path / 'planilhas' / 'clientes.xlsx', header=0)
print(clientsExcel.head(10))
print('======================\n\n\n')
#removing index column
print('removing index col')
clientsExcel = pd.read_excel(path / 'planilhas' / 'clientes.xlsx', index_col=0)
print(clientsExcel.head(10))
print('======================\n\n\n')
#reading a specific column
print('reading a specific column')
clientsExcel = pd.read_excel(path / 'planilhas' / 'clientes.xlsx', usecols='A:B')
print(clientsExcel.head(10))
print('======================\n\n\n')
import pandas as pd
from pathlib import Path

path = Path(__file__).parent
clientsExcel = pd.read_excel(path / 'planilhas' / 'clientes.xlsx', sheet_name=None)

for tab, table in clientsExcel.items():
    table.to_excel(path / f'{tab}.xlsx', index=None)

with pd.ExcelWriter(path / 'all.xlsx') as all:
    for file in Path(path).glob('*.xlsx'):
        table = pd.read_excel(file)
        table.to_excel(all, sheet_name=file.stem, index=False)

print(clientsExcel)
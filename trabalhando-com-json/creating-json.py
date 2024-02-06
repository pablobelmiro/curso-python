import json 
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

#creating json
data_json = '''
{
  "assinantes" : [
    {
      "nome": "Adriano Soares",
      "telefone": "51 99999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano faccioni",
      "telefone": "51 99999999",
      "email": "juliano@email.com",
      "em_dia": false
    }
    ],
  "data_extração": "2023/08/22"
}
'''

#converting json to dict
convertedJson = json.loads(data_json)
print(convertedJson)
print(type(convertedJson))
print('=====\n')

#converting dict to json
jsondumps = json.dumps(convertedJson, ensure_ascii=False, indent=2)
print(jsondumps)
print(type(jsondumps))
print('=====\n')

#reading .json file
path = Path(__file__).parent
with open(path / 'jsons' / 'assinantes.json') as item:
    memoryFile = json.load(item)

print(memoryFile)
print(type(memoryFile))

#writin a json
with open(path / 'output.json', 'w') as output:
    json.dump(memoryFile, output, indent=2, ensure_ascii=False)

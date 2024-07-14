import os
import shutil

import requests

root_cache_directory = f'{os.getcwd()}/cache'
files = [
    {"name": "Comercio", "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"},
    {"name": "ExpEspumantes", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv"},
    {"name": "ExpSuco", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"},
    {"name": "ExpUva", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv"},
    {"name": "ExpVinho", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"},
    {"name": "ImpEspumantes", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv"},
    {"name": "ImpFrescas", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv"},
    {"name": "ImpPassas", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv"},
    {"name": "ImpSuco", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"},
    {"name": "ImpVinhos", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv"},
    {"name": "ProcessaAmericanas", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"},
    {"name": "ProcessaMesa", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"},
    {"name": "ProcessaSemclass", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"},
    {"name": "ProcessaViniferas", "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"},
    {"name": "Producao", "url": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"}
]


def clear_cache():
    if (os.path.exists(root_cache_directory)):
        shutil.rmtree(root_cache_directory)


def build_cache():
    os.makedirs(root_cache_directory, exist_ok=True)
    for file in files:
        download(file["url"], file["name"])


def download(url, name):
    file = f'{root_cache_directory}/{name}'
    if os.path.exists(file):
        lines = open(file, 'r', encoding='iso-8859-1').read()
        print(f'{name} CSV found, checking... ', end='')
        if lines[-1] == '\n':
            print('OK.')
            return
        else:
            print('Invalid!')

    print(f'Downloading {url}... ', end='')

    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            with open(file, 'w', encoding='iso-8859-1') as file:
                file.write(content)
            print('Success!')
        else:
            print(f'Failed. Status code: {response.status_code}')
    except Exception as e:
        if os.path.exists(file):
            os.remove(file)
        print(f'Error downloading {url}: {str(e)}')

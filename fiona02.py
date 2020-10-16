import fiona

with fiona.open('datos/us-states.json', 'r') as estados:
    for registro_estado in estados:
        print(registro_estado['geometry'])
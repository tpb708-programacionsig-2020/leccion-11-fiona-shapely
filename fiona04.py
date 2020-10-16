import fiona
from shapely.geometry import shape

# Archivo de registros de presencia de especies
with fiona.open('datos/especies.geojson', 'r') as registros_presencia_especies:
    
    # Archivo de distritos de Curridabat
    with fiona.open('datos/curridabat-distritos-wgs84-ign-2019.geojson', 'r') as distritos:
        
        for registro_presencia_especie in registros_presencia_especies:
            for registro_distrito in distritos:
                if shape(registro_distrito['geometry']).contains(shape(registro_presencia_especie['geometry'])):
                    if (registro_presencia_especie['properties']['class'] == 'Aves'):
                        print(shape(registro_presencia_especie['geometry']), 
                              registro_presencia_especie['properties']['class'],
                              registro_presencia_especie['properties']['scientificName'],
                              registro_distrito['properties']['nom_distr'])
                        break
import fiona

from shapely.geometry import mapping, shape
from collections import OrderedDict
import logging

# Apertura del archivo de provincias (entrada)
with fiona.open('datos/provincias_snit.geojson', 'r') as provincias:
    
    # Esquema (estructura) del archivo de centroides
    esquema_centroides = {
        'geometry': 'Point',
        'properties': OrderedDict([
            ('provincia', 'str')
        ])
    }    
    
    # Apertura del archivo de centroides (salida)
    with fiona.open('datos/centroides_provincias.geojson', 'w',
                    crs=provincias.crs, 
                    driver="GeoJSON",
                    schema=esquema_centroides
                    ) as centroides:
        
        # Recorrido de las provincias
        for registro_provincia in provincias:
            try:
                # Construcción del registro de cada centroide
                registro_centroide = {
                    'geometry': {
                        'type': 'Point',
                        'coordinates': ((mapping(shape(registro_provincia['geometry']).centroid))['coordinates'][0],
                                        (mapping(shape(registro_provincia['geometry']).centroid))['coordinates'][1])
                    },
                    'properties': OrderedDict([
                        ('provincia', registro_provincia['properties']['nom_prov'])
                    ])
                }
                # Escritura del registro de cada centroide
                centroides.write(registro_centroide)        

                # Impresión de la geometría del centroide
                print(shape(registro_provincia['geometry']).centroid)
            except:
                logging.exception("Error al procesar el registro %s:", registro_provincia['id'])
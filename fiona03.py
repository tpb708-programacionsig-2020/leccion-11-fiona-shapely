# Centroides

import fiona
from shapely.geometry import mapping, shape

with fiona.open('datos/provincias_snit_crtm05.geojson', 'r') as provincias:
    for registro_provincias in provincias:
        print("Provincia:", registro_provincias['properties']['nom_prov'],
              "Centroide:", shape(registro_provincias['geometry']).centroid,
              "Área calculada:", shape(registro_provincias['geometry']).area/1000000,
              "Área reportada:", registro_provincias['properties']['area_km2']
              )
        

# Impresión de las coordenadas de los centroides        
#with fiona.open('datos/provincias_snit_crtm05.geojson', 'r') as provincias:
#    for registro_provincia in provincias:
#        print(mapping(shape(registro_provincia['geometry']).centroid)['coordinates'][0], 
#              mapping(shape(registro_provincia['geometry']).centroid)['coordinates'][1])        
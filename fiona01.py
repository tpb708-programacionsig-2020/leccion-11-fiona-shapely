import fiona

# Apertura del archivo
with fiona.open('datos/provincias_snit_crtm05.geojson', 'r') as provincias:
    
    # Recorrido de los registros
    for registro_provincia in provincias:
        print("Código:", registro_provincia['properties']['cod_prov'],
              "Nombre:", registro_provincia['properties']['nom_prov'],
              "Área:", '{:6.2f}'.format(registro_provincia['properties']['area_km2'])
              )
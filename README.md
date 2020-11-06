# Fiona y Shapely

El repositorio correspondiente a esta lección está disponible en [https://github.com/tpb708-programacionsig-2020/leccion-11-fiona-shapely/](https://github.com/tpb708-programacionsig-2020/leccion-11-fiona-shapely/). Se recomienda bifurcarlo a su cuenta en GitHub.

## Recursos
- Sitio oficial de Fiona: [Toblerity/Fiona: Fiona reads and writes geographic data files](https://github.com/Toblerity/Fiona)
- Sitio oficial de Shapely: [Toblerity/Fiona: Manipulation and analysis of geometric objects](https://github.com/Toblerity/Shapely)

## Notebooks
- [Fiona y Shapely](https://github.com/tpb708-programacionsig-2020/leccion-11-fiona-shapely/blob/master/fiona-shapely.ipynb)

## Creación de un ambiente Conda y clonación del repositorio
Ejecute estos comandos desde la línea de comandos de Anaconda, en el directorio en el que desea almacenar el repositorio clonado.
```shell
# Actualización de Conda
conda update -n base -c defaults conda

# Creación del ambiente
conda create -n leccion-11

# Activación del ambiente
conda activate leccion-11

# Instalación de módulos
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 shapely fiona jupyter

# Clonación del repositorio (debe sustituir la palabra "usuario" por su nombre de usuario en GitHub)
git clone https://github.com/usuario/leccion-11-fiona-shapely.git
cd leccion-11-fiona-shapely

# Ejecución de Jupyter Notebook
jupyter notebook

# Actualización del repositorio y de los archivos GeoJSON generados
$ git add .
$ git commit -m "Actualizar notebook"
$ git push

# Desactivación del ambiente Conda
$ conda deactivate
```

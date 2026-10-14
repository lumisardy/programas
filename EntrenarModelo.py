# Te sugiero antes de instalar nada, crear una entorno virtual.
# Asi tienes todas las librerias para este proyecto juntas y activas.
# Instala las librerias de ultralytics "pip install ultralytics"
from ultralytics import YOLO

# Carga el modelo YOLO11n
model = YOLO("yolo11n.pt")

# Entrena el modelo con el dataset
model.train(data="c:/ruta/dataset/imagenes/data.yaml",
    epochs=100, # Número de épocas
    imgsz=640, # Tamaño de entrada de la imagen
    patience=10) # Parada anticipada si no hay mejora


# Existe en internet una pagina que se llama roboflow para etiquetado.
# En el archivo data.yaml que estará en la ruta que ves arriba,
# veras que tiene esto si le abres con notepad
train: ../train/images
val: ../valid/images
test: ../test/images
nc: 2   # Número de etiquetas que tienen las imagenes para entrenar.
names: ['botella', 'lata'] 
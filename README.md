# MLT-project

Organización del proyecto:

1. <strong>data.ipynb :</strong> En este notebook se trabajó todo lo relacionado a los datos a utilizar. En este cuaderno se hizo el aumento de datos respectivo y 
se creó el dataset ArtUs (en formato HDFS). Se podrá encontrar ese archivo en este repositorio como data_art.h5 y contiene 15k imágenes con 5000 imágenes
por cada clase.

2. <strong>subBigGAN.ipynb</strong> En este notebook se trabajó la cGAN para realizar preentrenar el modelo. Se utilizaron los datos de CIFAR10 para hacer este pre
entrenamiento.

3. <strong>cArtGAN.ipynb</strong> En este notebook se creó la arquitectura correspondiente del paper y se entrenó sobre el conjunto de datos ArtUs.

4. <strong>cTransferArtGAN.ipynb</strong> En este notebook se creó la arquitectura correspondiente y se utilizó el modelo preentrenado "subBigGAN" como punto de arranque.
Se congelaron las capas de más bajo nivel y se agregaron dos capas extra para capturar otras características de los datos. Luego del transfer-learning, se entrenó con los datos
de ArtUs.

5. <strong>checkpoints/</strong> En esta carpeta están guardados todos los checkpoints del entrenamiento de los modelos 2-4. 

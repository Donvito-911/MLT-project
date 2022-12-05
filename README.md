# Conditional Generative Adversarial Nets in Painting Artwork

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

Los modelos fueron entrenados entre Colab y el ambiente de Nvidia (ambos con una GPU T4). 

# Despliegue de la aplicación
El archivo <strong>app.ipynb</strong> es un notebook que contiene ambos modelos y además una aplicación local y remota en Gradio. Esta aplicación permite escoger entre los 3 tipos de arte que utilizamos (abstracto, islámico y geométrico) y además el tipo de modelo: "Scratch Model" hace referencia al modelo entrenado desde cero y "Transfer-learning model" hace referencia al modelo que fue además pre-entrenado con el dataset de CIFAR10.

En este link (https://6e8eb49350d8db91.gradio.app/) se encuentra la aplicacón desplegada en remoto hasta el 6 de diciembre.

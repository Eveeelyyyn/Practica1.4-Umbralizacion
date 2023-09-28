# Umbralización de Imágenes en Python 📸

![Ejemplo de Imagen Umbralizada](imagen_ejemplo.png)

Bienvenidos a nuestro proyecto de umbralización de imágenes en Python. En este trabajo, hemos desarrollado un programa que implementa diversas técnicas de umbralización de imágenes. Estas técnicas permiten procesar imágenes en escala de grises y obtener resultados de segmentación efectivos.

## Técnicas de Umbralización Implementadas
En este proyecto, hemos implementado las siguientes técnicas de umbralización:

1. **Umbralización Global:** Este método utiliza un valor de umbral fijo para separar píxeles de una imagen en dos categorías: píxeles por debajo del umbral y píxeles por encima del umbral. Es una técnica básica pero útil en muchas aplicaciones.

2. **Umbralización Global por el Método de Otsu:** El método de Otsu es una técnica de umbralización automática que determina un valor de umbral óptimo. Maximiza la varianza entre las dos clases de píxeles (fondo y objeto) para obtener una segmentación precisa.

3. **Umbralización Local Adaptativa por el Método de Bernsen:** Este método divide la imagen en regiones más pequeñas y aplica un umbral local en cada región. Esto permite adaptarse a las variaciones locales de intensidad en la imagen, lo que es útil en situaciones donde la iluminación es desigual.

## Visualización de Resultados
Para que puedas evaluar fácilmente los resultados de cada técnica, hemos utilizado la biblioteca Matplotlib para mostrarlos en una sola imagen. Cada resultado se presenta en un subplot separado, lo que facilita la comparación y evaluación de las diferentes técnicas.

![Resultados de Umbralización](resultados.png)

## Cómo Usar el Programa
Aquí te proporcionamos instrucciones sobre cómo utilizar nuestro programa:
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas necesarias instaladas.
3. Ejecuta el programa y proporciona una imagen en escala de grises como entrada.
4. El programa aplicará las técnicas de umbralización y mostrará los resultados utilizando Matplotlib.

## Autores
Este proyecto fue realizado por un equipo apasionado de desarrolladores:
- [Aranza Michelle Gutierrez Jimenez](https://github.com/AranzaMich)
- [Evelyn Solano Portillo](https://github.com/Eveeelyyyn)
- [Marco Castelan Rosete](https://github.com/marco2220x)
- [Daniel Vega Rodríguez](https://github.com/DanVer2002)

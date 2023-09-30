# Umbralización de Imágenes en Python 📸

![Ejemplo de Imagen Umbralizada](/imagenesREADME/Figure1.jpeg)

En este trabajo, se ha desarrollado un programa que implementa diversas técnicas de umbralización de imágenes. Estas técnicas permiten procesar imágenes en escala de grises y obtener resultados de segmentación efectivos.

## Técnicas de Umbralización Implementadas
Técnicas de umbralización:

1. **Umbralización Global:** Este método utiliza un valor de umbral fijo para separar píxeles de una imagen en dos categorías: píxeles por debajo del umbral y píxeles por encima del umbral. Es una técnica básica pero útil en muchas aplicaciones.

2. **Umbralización Global por el Método de Otsu:** El método de Otsu es una técnica de umbralización automática que determina un valor de umbral óptimo. Maximiza la varianza entre las dos clases de píxeles (fondo y objeto) para obtener una segmentación precisa.

3. **Umbralización Local Adaptativa por el Método de Bernsen:** Este método divide la imagen en regiones más pequeñas y aplica un umbral local en cada región. Esto permite adaptarse a las variaciones locales de intensidad en la imagen, lo que es útil en situaciones donde la iluminación es desigual.

## Visualización de Resultados
Para que puedas evaluar fácilmente los resultados de cada técnica, hemos utilizado la biblioteca Matplotlib para mostrarlos en una sola imagen. Cada resultado se presenta en un subplot separado, lo que facilita la comparación y evaluación de las diferentes técnicas.

**Resultados obtenidos a partir de implementar los Métodos de Umbralización Global, Umbralización Global por Otsu y Umbralización Local Adaptativa por el Método de Bernsen**

![Resultados de Umbralización](/imagenesResultados/Figure1.jpeg)

![Resultados de Umbralización](/imagenesResultados/Figure2.jpeg)

![Resultados de Umbralización](/imagenesResultados/Figure3.jpeg)

**Resultados obtenidos a partir de implementar el Algoritmo Etiquetado de Componentes Conectados**

![Resultados de Etiquetado de Componentes Conectados](/imagenesResultados/Figure4.jpeg)

![Resultados de Etiquetado de Componentes Conectados](/imagenesResultados/Figure5.jpeg)

![Resultados de Etiquetado de Componentes Conectados](/imagenesResultados/Figure6.jpeg)

![Resultados de Etiquetado de Componentes Conectados](/imagenesResultados/Figure7.jpeg)

![Resultados de Etiquetado de Componentes Conectados](/imagenesResultados/Figure8.jpeg)

## Cómo Usar el Programa
Aquí te proporcionamos instrucciones sobre cómo utilizar nuestro programa:
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas necesarias instaladas.
3. Ejecuta el programa y proporciona una imagen en escala de grises como entrada.
4. El programa aplicará las técnicas de umbralización y mostrará los resultados utilizando Matplotlib.

## Autores
Este proyecto fue realizado por un equipo de estudiantes:
| [<img src="https://avatars.githubusercontent.com/u/113084234?v=4" width=115><br><sub>Aranza Michelle Gutierrez Jimenez</sub>](https://github.com/AranzaMich) |  [<img src="https://avatars.githubusercontent.com/u/113297618?v=4" width=115><br><sub>Evelyn Solano Portillo</sub>](https://github.com/Eveeelyyyn) |  [<img src="https://avatars.githubusercontent.com/u/112792541?v=4" width=115><br><sub>Marco Castelan Rosete</sub>](https://github.com/marco2220x) | [<img src="https://avatars.githubusercontent.com/u/113079687?v=4" width=115><br><sub>Daniel Vega Rodríguez</sub>](https://github.com/DanVer2002) |
| :---: | :---: | :---: | :---: |


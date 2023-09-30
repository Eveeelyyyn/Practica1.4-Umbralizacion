import cv2
import matplotlib.pyplot as plt
from segmentación.globalT import global_threshold
from segmentación.otsu import otsu
from segmentación.bernsen import bernsen
from formas_binarias.ComponentesConectados import CCL



if __name__ == "__main__":
   
    original_image = cv2.imread('utilidades/person_bacteria.jpeg', cv2.IMREAD_GRAYSCALE)

    thresholded_global_image =global_threshold(original_image)
    thresholded_otsu_image =otsu(original_image)
    thresholded_bernsen_image =bernsen(original_image, cmin=15, n=15, bg="bright")

    thresholded_global_CCL = CCL(thresholded_global_image)
    thresholded_otsu_CCL = CCL(thresholded_otsu_image)
    thresholded_bernsen_CCL = CCL(thresholded_bernsen_image)

    
    fig, axes = plt.subplots(1, 4, figsize=(12, 8))

    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title('Imagen original')
    axes[0].axis('off')

    axes[1].imshow(thresholded_global_image, cmap='gray')
    axes[1].set_title('Umbral global')
    axes[1].axis('off')

    axes[2].imshow(thresholded_otsu_image, cmap='gray')
    axes[2].set_title('Umbral por Otsu')
    axes[2].axis('off')

    axes[3].imshow(thresholded_bernsen_image, cmap='gray')
    axes[3].set_title('Umbral por Bernsen')
    axes[3].axis('off')

    plt.tight_layout()

    plt.show()

    
    fig, axes = plt.subplots(1, 4, figsize=(12, 8))

    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title('Imagen original')
    axes[0].axis('off')

    axes[1].imshow(thresholded_global_CCL)
    axes[1].set_title('Umbral global')
    axes[1].axis('off')

    axes[2].imshow(thresholded_otsu_CCL)
    axes[2].set_title('Umbral por Otsu')
    axes[2].axis('off')

    axes[3].imshow(thresholded_bernsen_CCL)
    axes[3].set_title('Umbral por Bernsen')
    axes[3].axis('off')

    plt.tight_layout()

    plt.show()
    

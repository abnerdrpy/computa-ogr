import cv2
# Carregar imagem
img = cv2.imread("consolidation_exercises/afolou.jpeg")
# Exibir imagem em uma janela
cv2.imshow("Minha imagem",img)
# Espera até pressionar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
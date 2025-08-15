import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# funções desenvolvidas para manipular as imagens
def carregarImagem(caminho: str) -> np.ndarray:
    imagemRGB = Image.open(caminho)
    imagemRGBA = imagemRGB.convert("RGBA")
    return np.array(imagemRGBA)

def salvarImagem(matrizImagem: np.ndarray, caminho: str):
    imagem = Image.fromarray(matrizImagem.astype(np.uint8))
    imagem.save(caminho)

def exibirImagem(imagem, titulo, tamanho):
    plt.figure(figsize=tamanho)
    plt.imshow(imagem)
    plt.axis("off")
    plt.title(titulo)
    plt.show()

def converterEscalaCinza(matrizImagemRGBA: np.ndarray):
    pesosRGBA = np.array([0.2989, 0.5870, 0.1140, 0])
    matrizImagemCinza = matrizImagemRGBA[...,:4] @ pesosRGBA
    return matrizImagemCinza
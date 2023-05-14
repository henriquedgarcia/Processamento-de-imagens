from PIL import Image
from PIL.PyAccess import PyAccess
import math


def main():
    filtro_espacial_detec_borda_hor = [[-1, 0, 1],
                                       [-2, 0, 2],
                                       [-1, 0, 1]]
    filtro_espacial_media = [[1 / 9, 1 / 9, 1 / 9],
                             [1 / 9, 1 / 9, 1 / 9],
                             [1 / 9, 1 / 9, 1 / 9]]

    filtro_espacial_media_gaussiana = [[1 / 16, 2 / 16, 1 / 16],
                                       [2 / 16, 4 / 16, 2 / 16],
                                       [1 / 16, 2 / 16, 1 / 16]]

    filtro_espacial_media_2 = [[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                               [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                               [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                               [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                               [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]]

    imagem = Image.open("fig_3.bmp")
    new_image = roda_filtro(imagem, filtro_espacial_media_gaussiana, correlacao)
    # new_image.show()
    new_image.save("teste_2.png")


def roda_filtro(imagem: Image, filtro: list, operacao):
    borda = int(math.floor(len(filtro) / 2.))
    imagem_com_borda = cria_borda(imagem, borda=borda)

    imagem_int32 = imagem.convert("I")
    pixels = imagem_int32.load()

    largura, altura = imagem.size
    for y in range(borda, altura):
        for x in range(borda, largura):
            area = imagem_com_borda.crop((x - borda, y - borda, x + borda + 1, y + borda + 1))
            novo_valor = operacao(area, filtro)
            imagem_int32.putpixel((x, y), novo_valor)
    imagem_int32 = imagem_int32.convert(mode="L")

    return remove_borda(imagem_int32)


def cria_borda(img: Image, borda=1):
    largura, altura = img.size
    image_preenchida = Image.new(mode="L", size=(largura + 2 * borda, altura + 2 * borda), color=0)
    image_preenchida.paste(img, (borda, borda, largura + borda, altura + borda))
    return image_preenchida


def remove_borda(image_com_borda: Image, borda=1):
    largura, altura = image_com_borda.size
    imagem_cortada = image_com_borda.crop((borda, borda, largura - borda - 1, altura - borda - 1))
    return imagem_cortada


def correlacao(imagem: Image, filtro: list):
    largura, altura = imagem.size
    pixels = imagem.load()
    acumulador = 0
    for y in range(altura):
        for x in range(largura):
            acumulador += pixels[x, y] * filtro[x][y]
    return int(acumulador)


def convolucao(imagem: Image, filtro: list):
    largura, altura = imagem.size
    pixels = imagem.load()
    acumulador = 0
    for y in range(altura):
        for x in range(largura):
            acumulador += pixels[x, y] * filtro[largura - 1 - x][altura - 1 - y]
    return acumulador


if __name__ == '__main__':
    main()

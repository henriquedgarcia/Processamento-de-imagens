from PIL import Image
from PIL.PyAccess import PyAccess
import math


def main():
    """
    Considere a figura “fig1.bmp” disponível em
    https://drive.google.com/file/d/1-2ecGWTYHjJPCrHSijWmqr5CGmT22rXz/view?usp=sharing.
    Existe uma imagem oculta nos seus dois primeiros bits. Crie um script em Python para
    extrair e salvar essa imagem. Em seguida aplique um filtro de limiar na imagem extraída
    com valor de corte igual a 150 de forma que a imagem extraída seja clara e legível.
    Por fim, copie e cole o seu código na resposta desta questão. OBS: O código deve rodar
    no computador do professor.
    :return:
    """
    img = Image.open("fig1.bmp")
    nova_imagem = Image.new("L", img.size, 0)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            img1_pixel = img.getpixel((x, y))
            img1_4bits = img1_pixel & int('11111100', 2)
            img2_shift = img2.getpixel((x, y)) >> 4
            novo_pixel = img1_4bits | img2_shift
            nova_imagem.putpixel((x, y), novo_pixel)

    nova_imagem.show()
    nova_imagem.save("imagem_ocultada.bmp")


def aparece():
    img = Image.open("../Recursos extra/Ocultação/imagem_ocultada.bmp")
    largura, altura = img.size
    nova_imagem = Image.new("L", (largura, altura), 0)

    for x in range(largura):
        for y in range(altura):
            img_pixel = img.getpixel((x, y))
            img_2bits = img_pixel & int('00001111', 2)
            img2_shift = img_2bits << 4
            nova_imagem.putpixel((x, y), img2_shift)
    nova_imagem.save("extracao.bmp")

if __name__ == '__main__':
    # main()
    aparece()

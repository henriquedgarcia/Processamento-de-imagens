from PIL import Image


def main():
    # exerc01()
    # exerc02()
    # exerc03()
    exerc04()


def exerc01():
    """"
    Abra o arquivo “lista_1_fig1.tif”, imprima o formato, o modo e a resolução
    da figura  no terminal, exiba a imagem e salve a imagem no formato JPG. Tire
    todos os prints (código, terminal e pasta contendo a figura) na mesma
    janela.
    """
    filename = 'lista_1_fig1.tif'
    im = Image.open(filename)
    print(im.mode, im.size, im.format)
    im.save('resultado_exerc01.jpg', )
    im.show()


def exerc02():
    """
    Abra o arquivo “lista_1_fig1.tif”, recorte um retângulo da figura com as
    coordenadas (350, 350, 850, 850), rode este recorte 180° e cole nas
    coordenadas (0, 0, 500, 500). Salve a imagem como PNG e exiba a imagem.
    Tire todos os prints (código e a pasta contendo a figura e a figura) na
    mesma janela.
    """
    filename = 'lista_1_fig1.tif'
    im = Image.open(filename)
    box = (350, 350, 850, 850)
    region = im.crop(box)
    region = region.transpose(Image.Transpose.ROTATE_180)
    box = (0, 0, 500, 500)
    im.paste(region, box)

    im.save('resultado_exerc02.png')
    im.show()


def exerc03():
    """
    Abra o arquivo “lista_1_fig2.tif”, aumente sua resolução para 1024x1024
    pixeis. Converta a imagem para modo L (escala de cinza). Rode a imagem 45°
    em sentido anti-horário. Salve a imagem como BMP e exiba a imagem.
    """
    filename = 'lista_1_fig2.tif'
    im = Image.open(filename)
    im = im.resize([1024, 1024])
    im = im.convert("L")
    im = im.rotate(45)

    im.save('resultado_exerc03.bmp')
    im.show()


# exerc03()


def exerc04():
    """"
    Alteração de brilho: Escreva um programa que carrega uma imagem, converte a imagem para escala de cinza
    e altera o brilho da imagem, aumentando ou diminuindo o valor de cada pixel. Por
    exemplo, se um pixel tiver o valor (150) e quisermos aumentar o
    brilho em 20%, podemos adicionar 20% na componente, tornando-o
    (180).

    """
    filename = 'lista_1_fig2.tif'
    im = Image.open(filename)
    im = im.convert('L')
    pix = im.load()
    razao = 1.2

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            novo_valor = pix[x, y] * razao
            if novo_valor > 255:
                novo_valor = 255
            pix[x, y] = int(novo_valor)

    im.show()
    im.save('resultado_exerc04.jpg')


if __name__ == '__main__':
    main()

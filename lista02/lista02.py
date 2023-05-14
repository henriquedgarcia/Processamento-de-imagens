from PIL import Image, ImageFilter


def main():
    exerc01()
    exerc02()
    exerc03()


def exerc01():
    """"
    1)	Inverter uma imagem: Abra o arquivo “fig_1.tif”. Crie um Mapa de pixel.
    Para cada pixel, subtraia 255 do valor do pixel e coloque o resultado de
    volta na mesma posição. Salve a imagem no formato png e exiba a imagem. Tire
    todos os prints (código e figura) na mesma janela.
    """
    filename = 'fig_1.tif'
    img = Image.open(filename)
    pixels = img.load()

    for i in range(img.size[0]):  # for every col:
        for j in range(img.size[1]):  # For every row
            pixels[i, j] = 255 - pixels[i, j]

    img.save('resultado_exerc01.png')
    img.show()


def exerc02():
    """
    2)	Realizar uma operação de limiar: Abra o arquivo “fig_2.tif”. Crie um
    mapa de pixel. Para cada pixel, atribua 0 se a intensidade for menor do que
    127. Caso contrário, atribua 255. Salve a imagem como PNG e exiba a imagem.
    Tire todos os prints (código e a pasta contendo a figura e a figura) na
    mesma janela. Tire todos os prints (código e figura) na mesma janela.
    """
    filename = 'fig_2.tif'
    img = Image.open(filename)
    pixels = img.load()

    for i in range(img.size[0]):  # for every col:
        for j in range(img.size[1]):  # For every row
            if pixels[i, j] > 127:
                pixels[i, j] = 255
            else:
                pixels[i, j] = 0

    img.save('resultado_exerc02.png')
    img.show()


def exerc03():
    """
    3)	Aplicar alguns filtros: Abra o arquivo “fig_3.tif”. Crie uma imagem em
    branco de tamanho 400x400. Aplique os filtros BLUR, FIND_EDGES e EMBOSS.
    Cole a imagem original e as 3 novas imagens na imagem em branco criada,
    como no arranjo abaixo. Tire todos os prints (código e figura) na mesma
    janela.
    """
    filename = 'fig_3.tif'
    im = Image.open(filename)
    img_blur = im.filter(ImageFilter.BLUR)
    img_edges = im.filter(ImageFilter.FIND_EDGES)
    img_emboss = im.filter(ImageFilter.EMBOSS)

    new_image = Image.new('L', (400, 400), "black")
    new_image.paste(im, (0, 0, 200, 200))
    new_image.paste(img_blur, (200, 0, 400, 200))
    new_image.paste(img_edges, (0, 200, 200, 400))
    new_image.paste(img_emboss, (200, 200, 400, 400))
    new_image.show()
    im.save('resultado_exerc03.bmp')


if __name__ == '__main__':
    main()
    print('Fim execício')

from PIL import Image, ImageFilter


def main():
    # exerc01()
    # exerc02()
    exerc03()


def exerc01():
    """"
    1)  Alteração de brilho: Usando a imagem “mandril_color.tif”, escreva um
    programa que carrega uma imagem e altera o brilho da imagem, aumentando ou
    diminuindo o valor de cada pixel RGB. Por exemplo, se um pixel tiver o valor
    (50, 100, 150) e quisermos aumentar o brilho em 20%, podemos adicionar 20% a
    cada componente RGB, tornando-o (60, 120, 180).
    """
    filename = 'mandril_color.tif'
    img = Image.open(filename)
    pixels = img.load()
    fator_brilho = 5

    for i in range(img.size[0]):  # for every col:
        for j in range(img.size[1]):  # For every row
            # pega as tres cores do pixel da posição (i, j)
            r, g, b = pixels[i, j]

            # multiplica o valor de cada cor pelo fator de brilho. Provavelmente o
            # resultado é real e deve ser convertido para inteiro posteriormente.
            r = r * fator_brilho
            g = g * fator_brilho
            b = b * fator_brilho

            # Verifica se o novo valor será maior do que 255 ou menor do que 0.
            # Se for maior do que 255 atribui valor 255. Caso seja menor do que
            # 0 atribui o valor 0. Caso contrário converte o numero para inteiro.
            r = 255 if r > 255 else 0 if r < 0 else int(r)
            g = 255 if r > 255 else 0 if g < 0 else int(g)
            b = 255 if r > 255 else 0 if b < 0 else int(b)

            # Atribui o valor do pixel de volta à imagem.
            pixels[i, j] = (r, g, b)

    img.show()
    img.save('resultado_exerc01.png')


def exerc02():
    """
    2)	Conversão de cores: Usando a imagem “peppers_color.tif”, escreva um
    programa que carrega uma imagem em RGB e converta-a manualmente para uma
    imagem em escala de cinza. Isso pode ser feito alterando o valor de cada
    pixel para a média dos componentes R, G e B.
    """

    # A imagem está com problema. Então, antes de fazer o exercício, abrimos ela no Paint e salvamos como bmp.
    filename = 'peppers_color.bmp'
    img = Image.open(filename)
    img_resultante = Image.new('L', img.size, 0)

    pixels = img.load()
    img_resultante_pixel = img_resultante.load()

    for x in range(img.size[0]):  # for every col:
        for y in range(img.size[1]):  # For every row
            r, g, b = pixels[x, y]
            media = int((r + g + b) / 3)
            img_resultante_pixel[x, y] = media

    img_resultante.save('resultado_exerc02.png')
    img_resultante.show()


def exerc03():
    """
    3)	Subtração de imagens: Considere as imagens fig2a.tiff e fig2b.tiff que são
    dois quadros diferentes de um mesmo vídeo. Realize a subtração pixel a pixel e
    exiba o resultado para ver como os pixels.
    """
    im1 = Image.open('fig2a.tiff')
    im2 = Image.open('fig2b.tiff')
    new_image = Image.new('L', im1.size, 0)

    for x in range(im1.size[0]):  # for every col:
        for y in range(im1.size[1]):  # For every row
            pix1 = im1.getpixel((x, y))
            pix2 = im2.getpixel((x, y))

            # Devemos atribuir o valor absoluto, ou seja, ignorar o sinal, uma vez que as
            # imagens não podem ter valor negativo.
            new_image.putpixel((x, y), abs(pix1 - pix2))

    new_image.save('resultado_exerc03.bmp')
    new_image.show()


if __name__ == '__main__':
    main()
    print('Fim da lista 03')

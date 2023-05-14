from PIL import Image


def main():
    # ex1()
    ex2()
    # ex3()
    # ex4()


def ex1():
    """
    Operação Negativo. Considere a imagem em escala de cinza fig1.tif e aplique a função
    de negativo. Mas antes, crie uma tabela de lookup e faça a transformação aplicando a
    tabela
    :return:
    """
    img = Image.open("fig_1.tif")
    largura, altura = img.size

    # A tabela de lookup cria uma tabela para a transformação dos pixels. Isso evita de ficar repetindo cálculos.
    # Depois de descobrir quais os valores para cada valor dos pixels basta aplicar a tabela para descobrir
    # o novo valor.
    lookup = {}
    for x in range(256):
        lookup[x] = 255 - x

    for x in range(largura):
        for y in range(altura):
            valor = img.getpixel((x, y))
            novo_valor = lookup[valor]
            img.putpixel((x, y), novo_valor)

    img.save('resultado_exerc01.png')
    img.show()


def ex2():
    """
    Operação Gama. Considere as imagens fig3.tif e fig2.tif. Aplique a função de correção
    de gama apresentada abaixo para L = 256 e encontre um valor para o gama coerente
    que torne o realce das imagens adequado. Valores coerentes variam de 0.05 a 25.0.
    Não esqueça de converter os valores para inteiro.
    :return:
    """

    def gama(g, r):
        return 255 ** (1 - g) * r ** g

    # Primeiro fazemos a tabela de lookup aplicando a função gama para
    # todos os valores possíveis. Os valores devem ser arredondados e
    # convertidos para inteiro.
    lookup = {}
    for x in range(256):
        # para gama entre 0 e 1 a imagem clareia.
        # para gama entre 1 e inf, a imagem escurece.
        lookup[x] = int(round(gama(0.5, x)))

    # convertemos a imagem para cinza, pois ela é RGB
    img = Image.open("fig_3.tif")
    img = img.convert('L')

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # Aplicamos a tabela de lookup para encontrar o novo valor baseado na função gama.
            valor = img.getpixel((x, y))
            novo_valor = lookup[valor]
            img.putpixel((x, y), novo_valor)

    img.save('resultado_exerc02.png')
    img.show()


def ex3():
    """
    Funções lineares definidas por partes. Considere a imagem fig4.tif e aplique os três
    tipos de funções Lineares apresentados na aula: alargamento de contraste, fatiamento
    e enfatização para os pontos:
    a. Alargamento: [(100,50), (150, 200)],
    b. Fatiamento: [(100,200), (150, 200)]
    c. Enfatização: [(100,200), (150, 200)]
    :return:
    """
    img = Image.open("fig4.tif")
    largura, altura = img.size
    pix_map = img.load()
    lookup_a = {}  # Alargamento 1
    lookup_b = {}  # Alargamento 2
    lookup_c = {}
    lookup_d = {}
    lookup_e = {}
    for x in range(255):
        lookup_a[x] = int(round(x / 2))
        lookup_b[x] = int(round(3 * x - 250))
        lookup_c[x] = int(round((11 * x + 2556) / 21))
        lookup_d[x] = 200 if 100 <= x <= 200 else 0
        lookup_e[x] = 200 if 100 <= x <= 150 else x

    for x in range(largura):
        for y in range(altura):
            valor = pix_map[x, y]
            if valor < 100:
                pix_map[x, y] = lookup_a[valor]
            elif valor < 150:
                pix_map[x, y] = lookup_b[valor]
            else:
                pix_map[x, y] = lookup_c[valor]
            # pix_map[x, y] = lookup_d[valor]
            # pix_map[x, y] = lookup_e[valor]

    img.show()


def ex4():
    """
    Fatiamento por plano de bits. Considere a imagem fig5.tif e extraia todos os 8 planos
    de bits. Em seguida, reconstrua a imagem com o plano 8, com o plano 8 e 7 e com o
    plano 8, 7 e 6.
    :return:
    """
    img = Image.open("fig5.tif")
    largura, altura = img.size
    pix_map = img.load()
    plano_8 = {}
    plano_7e8 = {}
    plano_6e7e8 = {}

    for x in range(255):
        plano_6e7e8[x] = x & int('11100000', 2)
        plano_7e8[x] = x & int('11000000', 2)
        plano_8[x] = x & int('10000000', 2)

    for x in range(largura):
        for y in range(altura):
            valor = pix_map[x, y]
            pix_map[x, y] = plano_6e7e8[valor]

    img.show()


if __name__ == "__main__":
    main()

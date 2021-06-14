
# \u2B1B e \u2b1c

"""
Para utilizar:

Criar a barra através do:

{nome} = create_bar(tamanho, número de passos por iteração, valor inicial)

Caso tamanho = 0 a barra encherá de 5 em 5

Após isso utilizar bar_print(bar) em cada iteração.
"""


def create_bar(tamanho=0, passo=1,  contagem=0):
    if tamanho:
        while contagem in range(tamanho):
            contagem += passo
            string_bar = '\r' + '\u2B1B' * contagem + '\u2b1c' * (tamanho - contagem) + ' | %d/%d' % (contagem, tamanho)
            yield string_bar
    else:
        total = contagem
        while True:
            contagem += passo
            total += passo
            if contagem > 5:
                contagem = 1
            string_bar = '\r' + '\u2B1B' * contagem + '\u2b1c' * (5 - contagem) + ' | %d' % (total)
            yield string_bar


def bar_print(barra):
    print(next(barra), end='')

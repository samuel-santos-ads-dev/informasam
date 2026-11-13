
import logo
import system_info
import colors


def obter_informacoes():
    informacoes = [
        ("OS:", system_info.distro()),
        ("Kernel:", system_info.kernel()),
        ("Host:", system_info.nome_maquina()),
        ("Arquitetura:", system_info.arquitetura()),
        ("CPU:", system_info.processador()),
        ("Memória RAM:", str(round(system_info.memoria_total(), 2)) + " GiB"),
        ("Disponível:", str(round(system_info.memoria_disponivel(), 2)) + " GiB"),
        ("Utilizada:", str(round(system_info.memoria_utilizada(), 2)) + " GiB"),
        ("Núcleos:", str(system_info.nucleos_cpu())),
        ("Threads:", str(system_info.threads_cpu())),
        ("Frequência:", str(round(system_info.frequencia_cpu(), 2)) + " GHz")
    ]

    return informacoes


def formatar_informacoes(informacoes):
    largura_rotulo = max(len(rotulo) for rotulo, valor in informacoes)

    lista_formatada = []

    for rotulo, valor in informacoes:
        rotulo = rotulo.ljust(largura_rotulo + 2)
        rotulo = colors.verde + colors.negrito + rotulo + colors.reset

        lista_formatada.append((rotulo, valor))

    return lista_formatada


def centralizar_lista(lista, tamanho):
    diferenca = tamanho - len(lista)
    espacos = diferenca // 2
    espacos_extras = diferenca % 2

    lista_centralizada = (
        [""] * espacos
        + lista
        + [""] * (espacos + espacos_extras)
    )

    return lista_centralizada


def main():
    informacoes = obter_informacoes()
    informacoes = formatar_informacoes(informacoes)

    logo_linhas = logo.exibir_logo()

    tamanho = max(len(informacoes), len(logo_linhas))

    logo_final = centralizar_lista(logo_linhas, tamanho)
    informacoes_final = centralizar_lista(informacoes, tamanho)

    largura_logo = max(len(linha) for linha in logo_linhas)
    espacamento = 6

    for esquerda, direita in zip(logo_final, informacoes_final):
        if direita:
            rotulo, valor = direita
            direita = rotulo + valor
        else:
            direita = ""

        print(esquerda.ljust(largura_logo + espacamento) + direita)


if __name__ == "__main__":
    main()

import logo
import system_info
import colors

def obter_informacoes():
    informacoes = [
        colors.verde + colors.negrito + "OS: ".ljust(15) + colors.reset + system_info.distro(),
        colors.verde + colors.negrito + "Kernel: ".ljust(15) + colors.reset + system_info.kernel(),
        colors.verde + colors.negrito + "Host: ".ljust(15) + colors.reset + system_info.nome_maquina(),
        colors.verde + colors.negrito + "Arquitetura: ".ljust(15) + colors.reset + system_info.arquitetura(),
        colors.verde + colors.negrito + "CPU: ".ljust(15) + colors.reset + system_info.processador(),
        colors.verde + colors.negrito + "Memória RAM: ".ljust(15) + colors.reset + str(round(system_info.memoria_total(), 2)) + " GiB",
        colors.verde + colors.negrito + "Disponível: ".ljust(15) + colors.reset + str(round(system_info.memoria_disponivel(), 2)) + " GiB",
        colors.verde + colors.negrito + "Utilizada: ".ljust(15) + colors.reset + str(round(system_info.memoria_utilizada(), 2)) + " GiB",
        colors.verde + colors.negrito + "Núcleos: ".ljust(15) + colors.reset + str(system_info.nucleos_cpu()),
        colors.verde + colors.negrito + "Threads: ".ljust(15) + colors.reset + str(system_info.threads_cpu()),
        colors.verde + colors.negrito + "Frequência: ".ljust(15) + colors.reset + str(round(system_info.frequencia_cpu(), 2)) + " GHz"
    ]
    return informacoes

def centralizar_lista(lista, tamanho):
    diferenca = tamanho - len(lista)
    espacos = diferenca // 2
    espacos_extras = diferenca % 2

    lista_centralizada = [""] * espacos + lista + [""] * (espacos + espacos_extras)

    return lista_centralizada

def main():
    informacoes = obter_informacoes()
    logo_linhas = logo.exibir_logo()

    tamanho = max(len(informacoes), len(logo_linhas))

    logo_final = centralizar_lista(logo_linhas, tamanho)
    informacoes_final = centralizar_lista(informacoes, tamanho)


    for esquerda, direita in zip(logo_final, informacoes_final):
        print(esquerda.ljust(25), direita)

if(__name__ == "__main__"):
    main()